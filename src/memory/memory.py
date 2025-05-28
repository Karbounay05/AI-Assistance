import sqlite3

def save_fact(key, value):
    conn = sqlite3.connect("memory.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS facts (key TEXT, value TEXT)")
    cur.execute("INSERT INTO facts VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()
