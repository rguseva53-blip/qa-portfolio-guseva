import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "tasks.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_all_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, status, assignee, created_at, due_date, completed_at FROM tasks")
    rows = cur.fetchall()
    conn.close()
    return rows
