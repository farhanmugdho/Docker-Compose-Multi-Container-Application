import os
import time
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

DB = dict(
    host=os.environ["DB_HOST"],
    port=os.environ.get("DB_PORT", "5432"),
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
)


def get_conn():
    return psycopg2.connect(**DB)


def init_db():
    for _ in range(10):
        try:
            conn = get_conn()
            with conn, conn.cursor() as cur:
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS notes ("
                    "id SERIAL PRIMARY KEY, text TEXT NOT NULL, "
                    "created_at TIMESTAMP DEFAULT NOW())"
                )
            conn.close()
            return
        except psycopg2.OperationalError:
            time.sleep(2)
    raise RuntimeError("Database not reachable")


init_db()


@app.get("/api/health")
def health():
    try:
        conn = get_conn()
        with conn, conn.cursor() as cur:
            cur.execute("SELECT 1")
        conn.close()
        return jsonify(status="ok", database="connected")
    except Exception:
        return jsonify(status="error", database="down"), 500


@app.get("/api/notes")
def list_notes():
    conn = get_conn()
    with conn, conn.cursor() as cur:
        cur.execute("SELECT id, text FROM notes ORDER BY id DESC LIMIT 20")
        rows = cur.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "text": r[1]} for r in rows])


@app.post("/api/notes")
def add_note():
    text = (request.get_json(silent=True) or {}).get("text", "").strip()
    if not text:
        return jsonify(error="text required"), 400
    conn = get_conn()
    with conn, conn.cursor() as cur:
        cur.execute("INSERT INTO notes (text) VALUES (%s) RETURNING id", (text,))
        new_id = cur.fetchone()[0]
    conn.close()
    return jsonify(id=new_id, text=text), 201
