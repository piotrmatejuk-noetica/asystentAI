"""SQLite state store — tracks pending emails and bot conversation state."""
import sqlite3
import json
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent.parent))

from config import DB_PATH


def _conn():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    with _conn() as con:
        con.executescript("""
            CREATE TABLE IF NOT EXISTS emails (
                id          TEXT PRIMARY KEY,
                account     TEXT,
                from_addr   TEXT,
                subject     TEXT,
                body        TEXT,
                draft       TEXT,
                importance  INTEGER,
                category    TEXT,
                project     TEXT,
                status      TEXT DEFAULT 'pending',
                message_id  INTEGER,
                created_at  REAL DEFAULT (unixepoch())
            );

            CREATE TABLE IF NOT EXISTS bot_state (
                chat_id     TEXT PRIMARY KEY,
                state       TEXT DEFAULT 'idle',
                context     TEXT DEFAULT '{}'
            );
        """)


def save_email(data: dict):
    with _conn() as con:
        con.execute("""
            INSERT OR REPLACE INTO emails
            (id, account, from_addr, subject, body, draft, importance, category, project)
            VALUES (:id, :account, :from_addr, :subject, :body, :draft, :importance, :category, :project)
        """, data)


def get_email(email_id: str) -> dict | None:
    with _conn() as con:
        row = con.execute("SELECT * FROM emails WHERE id=?", (email_id,)).fetchone()
        return dict(row) if row else None


def update_email(email_id: str, **kwargs):
    sets = ", ".join(f"{k}=?" for k in kwargs)
    vals = list(kwargs.values()) + [email_id]
    with _conn() as con:
        con.execute(f"UPDATE emails SET {sets} WHERE id=?", vals)


def get_bot_state(chat_id: str) -> tuple[str, dict]:
    with _conn() as con:
        row = con.execute("SELECT state, context FROM bot_state WHERE chat_id=?", (chat_id,)).fetchone()
        if row:
            return row["state"], json.loads(row["context"])
        return "idle", {}


def set_bot_state(chat_id: str, state: str, context: dict = None):
    ctx = json.dumps(context or {})
    with _conn() as con:
        con.execute("""
            INSERT INTO bot_state (chat_id, state, context) VALUES (?, ?, ?)
            ON CONFLICT(chat_id) DO UPDATE SET state=excluded.state, context=excluded.context
        """, (chat_id, state, ctx))


init_db()
