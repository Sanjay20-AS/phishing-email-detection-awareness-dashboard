"""SQLite persistence for analysis history."""
import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "phishing_dashboard.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            sender TEXT,
            subject TEXT,
            score INTEGER NOT NULL,
            classification TEXT NOT NULL,
            result_json TEXT NOT NULL
        )
        """)
        conn.commit()

def save_analysis(result: dict):
    risk = result["risk"]
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO analyses(sender, subject, score, classification, result_json) VALUES (?, ?, ?, ?, ?)",
            (result["sender"], result["subject"], risk["score"], risk["classification"], json.dumps(result))
        )
        conn.commit()

def history(limit=100):
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, created_at, sender, subject, score, classification FROM analyses ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()
    return [dict(r) for r in rows]

def summary():
    with get_connection() as conn:
        total = conn.execute("SELECT COUNT(*) FROM analyses").fetchone()[0]
        avg = conn.execute("SELECT COALESCE(AVG(score),0) FROM analyses").fetchone()[0]
        rows = conn.execute(
            "SELECT classification, COUNT(*) AS count FROM analyses GROUP BY classification"
        ).fetchall()
    return {"total": total, "average_score": round(avg, 1), "by_classification": [dict(r) for r in rows]}
