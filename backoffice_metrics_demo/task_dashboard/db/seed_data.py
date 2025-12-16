import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "tasks.db"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        cur.executescript(f.read())

    tasks = [
        ("Задача 1", "done", "Иван",
         datetime.now() - timedelta(days=3),
         datetime.now() - timedelta(days=1),
         datetime.now() - timedelta(days=1)),
        ("Задача 2", "in_progress", "Мария",
         datetime.now() - timedelta(days=1),
         datetime.now() + timedelta(days=1),
         None),
    ]

    cur.executemany(
        """
        INSERT INTO tasks(title, status, assignee, created_at, due_date, completed_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (
                t,
                s,
                a,
                c.isoformat(),
                d.isoformat(),
                comp.isoformat() if comp else None,
            )
            for t, s, a, c, d, comp in tasks
        ],
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
