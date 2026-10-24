import numpy as np
import pandas as pd

from clean_data import ATTENDANCE_RANGE, NUMERIC_COLUMNS, SCORE_RANGE

ALLOWED_DOMAINS = {"Machine Learning", "Web Development", "Electronics", "Mechanical"}
ALLOWED_STATUS = {"Submitted", "Not Submitted"}
# Columns that identify/categorize a student; these must never be missing.
CRITICAL_COLUMNS = ["student_id", "name", "domain", "submission_status"]


def _result(name, passed, detail=""):
    return {"check": name, "passed": bool(passed), "detail": detail}


def check_student_ids(df):
    missing = int(df["student_id"].isna().sum())
    dupes = df.loc[df["student_id"].duplicated(keep=False), "student_id"].unique().tolist()
    return _result("Student IDs unique and non-missing", missing == 0 and not dupes,
                   f"{missing} missing, duplicated IDs: {dupes}")


def check_range(df, column, low, high):
    values = df[column].dropna()
    bad = df.loc[(df[column] < low) | (df[column] > high), "student_id"].tolist()
    return _result(f"{column} within [{low}, {high}]", not bad,
                   f"{len(values)} non-missing values checked, out-of-range IDs: {bad}")


def check_allowed(df, column, allowed):
    bad = df.loc[~df[column].isin(allowed), ["student_id", column]]
    return _result(f"{column} in allowed set {sorted(allowed)}", bad.empty,
                   f"violations: {bad.values.tolist()}")


def check_critical_missing(df):
    counts = {c: int(df[c].isna().sum()) for c in CRITICAL_COLUMNS}
    return _result(f"No missing values in critical columns {CRITICAL_COLUMNS}",
                   sum(counts.values()) == 0, f"missing counts: {counts}")


def check_numeric(df):
    problems = {}
    for col in NUMERIC_COLUMNS:
        if not pd.api.types.is_numeric_dtype(df[col]):
            problems[col] = "non-numeric dtype"
        elif np.isinf(df[col].dropna()).any():
            problems[col] = "contains inf"
    return _result(f"Numeric columns {NUMERIC_COLUMNS} hold valid numbers", not problems,
                   f"problems: {problems}")


def missing_value_report(df):
    """Informational (not pass/fail): non-critical gaps left unimputed on purpose."""
    return {c: int(v) for c, v in df[NUMERIC_COLUMNS].isna().sum().items() if v}


def validate_dataset(df):
    results = [
        check_student_ids(df),
        check_range(df, "attendance_percent", *ATTENDANCE_RANGE),
        check_range(df, "score", *SCORE_RANGE),
        check_allowed(df, "domain", ALLOWED_DOMAINS),
        check_allowed(df, "submission_status", ALLOWED_STATUS),
        check_critical_missing(df),
        check_numeric(df),
    ]
    return {"all_passed": all(r["passed"] for r in results), "checks": results,
            "unimputed_missing_numeric": missing_value_report(df)}
