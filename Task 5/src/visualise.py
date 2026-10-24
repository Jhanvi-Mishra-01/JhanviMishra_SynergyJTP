from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # no display needed
import matplotlib.pyplot as plt


def domain_average_score(df, out_dir):
    avg = df.groupby("domain")["score"].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(avg.index, avg.values, color="#4C78A8")
    ax.bar_label(bars, fmt="%.2f")
    ax.set_title("Average Score by Domain")
    ax.set_xlabel("Domain")
    ax.set_ylabel("Average score (0-10)")
    ax.set_ylim(0, 10)
    plt.setp(ax.get_xticklabels(), rotation=15, ha="right")
    fig.tight_layout()
    path = Path(out_dir) / "domain_average_score.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def attendance_vs_score(df, out_dir):
    data = df.dropna(subset=["attendance_percent", "score"])
    fig, ax = plt.subplots(figsize=(8, 5))
    for domain, grp in data.groupby("domain"):
        ax.scatter(grp["attendance_percent"], grp["score"], s=70, label=domain)
    for _, r in data.iterrows():
        ax.annotate(r["student_id"], (r["attendance_percent"], r["score"]),
                    textcoords="offset points", xytext=(5, 5), fontsize=8)
    ax.set_title(f"Attendance vs Score (n={len(data)}; rows with missing/invalid values excluded)")
    ax.set_xlabel("Attendance (%)")
    ax.set_ylabel("Score (0-10)")
    ax.grid(alpha=0.3)
    ax.legend(title="Domain", fontsize=8)
    fig.tight_layout()
    path = Path(out_dir) / "attendance_vs_score.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def submission_status_count(df, out_dir):
    counts = df["submission_status"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 5))
    bars = ax.bar(counts.index, counts.values, color=["#59A14F", "#E15759"][:len(counts)])
    ax.bar_label(bars)
    ax.set_title("Submission Status Count")
    ax.set_xlabel("Submission status")
    ax.set_ylabel("Number of students")
    ax.set_yticks(range(0, int(counts.max()) + 2))
    fig.tight_layout()
    path = Path(out_dir) / "submission_status_count.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path
