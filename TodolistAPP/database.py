import sqlite3

DATABASE = "notes.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()

    # Users table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Notes table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            user_id INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------- USER FUNCTIONS ----------

def add_user(username, password):
    conn = get_connection()

    try:
        cursor = conn.execute("""
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """, (username, password))

        conn.commit()

        user_id = cursor.lastrowid

        conn.close()

        return user_id

    except sqlite3.IntegrityError:
        conn.close()
        return None


def get_user(username):
    conn = get_connection()

    cursor = conn.execute("""
        SELECT * FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user


# ---------- NOTE FUNCTIONS ----------

def get_notes(user_id):
    conn = get_connection()

    cursor = conn.execute("""
        SELECT * FROM notes
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,))

    notes = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return notes


def add_note(title, content, user_id):
    conn = get_connection()

    cursor = conn.execute("""
        INSERT INTO notes (title, content, user_id)
        VALUES (?, ?, ?)
    """, (title, content, user_id))

    conn.commit()

    note_id = cursor.lastrowid

    conn.close()

    return note_id


def update_note(note_id, title, content, completed, user_id):
    conn = get_connection()

    conn.execute("""
        UPDATE notes
        SET title = ?, content = ?, completed = ?
        WHERE id = ? AND user_id = ?
    """, (title, content, completed, note_id, user_id))

    conn.commit()
    conn.close()


def delete_note(note_id, user_id):
    conn = get_connection()

    conn.execute("""
        DELETE FROM notes
        WHERE id = ? AND user_id = ?
    """, (note_id, user_id))

    conn.commit()
    conn.close()


create_tables()