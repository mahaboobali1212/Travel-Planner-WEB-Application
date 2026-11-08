import sqlite3
from pathlib import Path

DB_PATH = Path("database.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS trips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    persons INTEGER NOT NULL,
    days INTEGER NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    conn = get_db()
    try:
        conn.executescript(SCHEMA)
        conn.commit()
    finally:
        conn.close()
    add_new_columns()

def add_new_columns():
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE trips ADD COLUMN travel_mode TEXT DEFAULT 'car';")
    except sqlite3.OperationalError:
        pass

    try:
        cursor.execute("ALTER TABLE trips ADD COLUMN accom_category TEXT DEFAULT 'budget';")
    except sqlite3.OperationalError:
        pass

    try:
        cursor.execute("ALTER TABLE trips ADD COLUMN distance REAL DEFAULT 0;")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()
    print("Columns ensured: travel_mode, accom_category, distance")

if __name__ == "__main__":
    init_db()
    add_new_columns()
