from datetime import datetime
import pandas as pd
from .task_service import get_all_tasks


def load_tasks_df():
    rows = get_all_tasks()
    df = pd.DataFrame(
        rows,
        columns=["id", "title", "status", "assignee", "created_at", "due_date", "completed_at"],
    )
    for col in ["created_at", "due_date", "completed_at"]:
        df[col] = pd.to_datetime(df[col])
    return df


def calc_basic_metrics():
    df = load_tasks_df()
    total = len(df)
    done = len(df[df["status"] == "done"])
    in_progress = len(df[df["status"] == "in_progress"])
    return {
        "total_tasks": total,
        "done_tasks": done,
        "in_progress_tasks": in_progress,
    }
