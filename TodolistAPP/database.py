import sqlite3

DATABASE = "notes.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def get_notes():
    conn = get_connection()

    cursor = conn.execute("""
        SELECT * FROM notes
        ORDER BY id DESC
    """)

    notes = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return notes


def add_note(title, content):
    conn = get_connection()

    cursor = conn.execute("""
        INSERT INTO notes (title, content)
        VALUES (?, ?)
    """, (title, content))

    conn.commit()

    note_id = cursor.lastrowid

    conn.close()

    return note_id


def update_note(note_id, title, content, completed):
    conn = get_connection()

    conn.execute("""
        UPDATE notes
        SET title = ?, content = ?, completed = ?
        WHERE id = ?
    """, (title, content, completed, note_id))

    conn.commit()
    conn.close()


def delete_note(note_id):
    conn = get_connection()

    conn.execute("""
        DELETE FROM notes
        WHERE id = ?
    """, (note_id,))

    conn.commit()
    conn.close()


create_table()