import re
from pathlib import Path

import numpy as np
import pandas as pd

DOMAIN_ALIASES = {
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "web": "Web Development",
    "web dev": "Web Development",
    "web development": "Web Development",
    "electronics": "Electronics",
    "mechanical": "Mechanical",
}
SUBMITTED_ALIASES = {
    "yes": "Submitted", "y": "Submitted", "true": "Submitted", "1": "Submitted",
    "no": "Not Submitted", "n": "Not Submitted", "false": "Not Submitted", "0": "Not Submitted",
}
WORD_NUMBERS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10,
}
SCORE_RANGE = (0, 10)       # observed scale in the data: 0-10
ATTENDANCE_RANGE = (0, 100)
NUMERIC_COLUMNS = ["attendance_percent", "score", "study_hours", "height_cm", "weight_kg"]


def load_raw(path):

    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, na_values=[""])


def _to_number(value):
    if pd.isna(value):
        return np.nan
    text = str(value).strip().lower()
    if text in WORD_NUMBERS:
        return float(WORD_NUMBERS[text])
    match = re.fullmatch(r"(-?\d+(?:\.\d+)?)\s*(?:%|[a-z]*)", text)
    return float(match.group(1)) if match else np.nan


def standardize_text(series, aliases, name, log):
    key = series.str.strip().str.lower()
    mapped = key.map(aliases)
    unknown = series[mapped.isna() & series.notna()]
    changed = int((series.notna() & (series != mapped)).sum())
    log["standardized"][name] = {"values_changed": changed, "unrecognized": unknown.tolist()}
    return mapped


def parse_numeric(series, name, log):
    parsed = series.map(_to_number)
    needed_conversion = series.notna() & ~series.astype(str).str.fullmatch(r"-?\d+(\.\d+)?")
    unparseable = series[series.notna() & parsed.isna()]
    log["converted"][name] = {
        "values_converted": int(needed_conversion.sum()),
        "unparseable": unparseable.tolist(),
    }
    return parsed


def parse_height_cm(series, log):
    def convert(value):
        if pd.isna(value):
            return np.nan
        text = str(value).strip().lower()
        number = _to_number(text)
        if np.isnan(number):
            return np.nan
        if "cm" in text:
            return number
        if re.search(r"\bm\b|\dm$", text) or number < 3:   
            return round(number * 100, 1)
        return number
    out = series.map(convert)
    in_metres = series.notna() & ~series.astype(str).str.contains("cm", case=False)
    log["converted"]["height_cm"] = {
        "values_converted": int(in_metres.sum()),
        "unparseable": series[series.notna() & out.isna()].tolist(),
        "note": "Values in metres were multiplied by 100; 'cm' suffix stripped.",
    }
    return out


def parse_weight_kg(series, log):
    def convert(value):
        if pd.isna(value):
            return np.nan
        text = str(value).strip().lower()
        number = _to_number(text)
        if np.isnan(number):
            return np.nan
        return round(number * 0.45359237, 1) if "lb" in text else number
    out = series.map(convert)
    log["converted"]["weight_kg"] = {
        "values_converted": int(series.notna().sum() - series.astype(str).str.fullmatch(r"-?\d+(\.\d+)?").sum()),
        "unparseable": series[series.notna() & out.isna()].tolist(),
        "note": "'kg' suffix stripped; pounds would be converted at 0.45359237.",
    }
    return out


def flag_out_of_range(series, low, high, name, log):
    
    bad = series.notna() & ((series < low) | (series > high))
    log["invalid"][name] = {
        "range": [low, high],
        "count": int(bad.sum()),
        "values": series[bad].tolist(),
    }
    return series.mask(bad)


def clean_dataset(raw):
    
    log = {"standardized": {}, "converted": {}, "invalid": {}, "missing_after_cleaning": {}}
    df = raw.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()
    log["rows_before"] = len(df)


    exact = int(df.duplicated().sum())
    df = df.drop_duplicates()


    df["domain"] = standardize_text(df["domain"], DOMAIN_ALIASES, "domain", log)
    df["submitted"] = standardize_text(df["submitted"], SUBMITTED_ALIASES, "submitted", log)


    df["attendance_percent"] = parse_numeric(df["attendance_percent"], "attendance_percent", log)
    df["score"] = parse_numeric(df["score"], "score", log)
    df["study_hours"] = parse_numeric(df["study_hours"], "study_hours", log)
    df["height_cm"] = parse_height_cm(df["height"], log)
    df["weight_kg"] = parse_weight_kg(df["weight"], log)
    df = df.drop(columns=["height", "weight"])
    df = df.rename(columns={"submitted": "submission_status"})

    df["attendance_percent"] = flag_out_of_range(df["attendance_percent"], *ATTENDANCE_RANGE, "attendance_percent", log)
    df["score"] = flag_out_of_range(df["score"], *SCORE_RANGE, "score", log)
    for col in ["study_hours", "height_cm", "weight_kg"]:
        df[col] = flag_out_of_range(df[col], 0, np.inf, col, log)

   
    id_dupes = int(df.duplicated(subset="student_id").sum())
    df = df.drop_duplicates(subset="student_id", keep="first").reset_index(drop=True)
    log["duplicates_removed"] = {"exact_rows": exact, "same_student_id": id_dupes, "total": exact + id_dupes}

    
    log["missing_after_cleaning"] = {c: int(v) for c, v in df.isna().sum().items() if v}
    log["rows_after"] = len(df)
    return df, log
