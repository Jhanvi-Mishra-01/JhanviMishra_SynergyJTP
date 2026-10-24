import json
from pathlib import Path

import pandas as pd

from clean_data import NUMERIC_COLUMNS


def summarize(df, numeric_columns=None, naive_numeric=False):
    """Summarize a dataframe. For the raw data (all strings) set naive_numeric=True:
    stats then use plain pd.to_numeric, which shows how much cannot be parsed as-is."""
    summary = {
        "rows": int(len(df)),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "missing_values": {c: int(v) for c, v in df.isna().sum().items()},
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_student_ids": int(df["student_id"].duplicated().sum()),
        "dtypes": {c: str(t) for c, t in df.dtypes.items()},
    }
    stats = {}
    for col in numeric_columns or []:
        series = pd.to_numeric(df[col], errors="coerce") if naive_numeric else df[col]
        entry = series.describe().round(3).to_dict()
        entry = {k: (None if pd.isna(v) else v) for k, v in entry.items()}
        entry["unparseable_or_missing"] = int(series.isna().sum())
        stats[col] = entry
    summary["numeric_stats" + ("_naive_coercion" if naive_numeric else "")] = stats
    summary["categorical_counts"] = {
        c: {str(k): int(v) for k, v in df[c].value_counts(dropna=False).items()}
        for c in df.select_dtypes(include="object") if c not in ("student_id", "name")
    }
    return summary


def save_json(data, path):
    Path(path).write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
