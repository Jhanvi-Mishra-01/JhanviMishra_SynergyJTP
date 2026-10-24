import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from clean_data import NUMERIC_COLUMNS, clean_dataset, load_raw
from summarise import save_json, summarize
from validate_data import validate_dataset
from visualise import attendance_vs_score, domain_average_score, submission_status_count


def main(argv):
    if len(argv) != 3:
        print("Usage: python src/main.py <input_csv> <output_dir>")
        return 2
    input_csv, out_dir = argv[1], Path(argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        raw = load_raw(input_csv)                                    
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
        return 1

    raw_numeric = ["attendance_percent", "score", "study_hours"]
    before = summarize(raw, raw_numeric, naive_numeric=True)          
    save_json(before, out_dir / "summary_before.json")

    cleaned, log = clean_dataset(raw)                                 
    validation = validate_dataset(cleaned)                            

    cleaned.to_csv(out_dir / "cleaned_students.csv", index=False)     
    after = summarize(cleaned, NUMERIC_COLUMNS)
    after["validation"] = validation
    save_json(after, out_dir / "summary_after.json")

    domain_average_score(cleaned, out_dir)                            
    attendance_vs_score(cleaned, out_dir)
    submission_status_count(cleaned, out_dir)

    for c in validation["checks"]:
        print(("PASS " if c["passed"] else "FAIL ") + c["check"])
    print(f"Done. Outputs written to {out_dir}/")
    return 0 if validation["all_passed"] else 3


if __name__ == "__main__":
    sys.exit(main(sys.argv))