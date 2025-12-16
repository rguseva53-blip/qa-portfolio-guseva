CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT NOT NULL,
    assignee TEXT,
    created_at TEXT NOT NULL,
    due_date TEXT,
    completed_at TEXT
);
