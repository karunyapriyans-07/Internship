from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# ---------------------------------------
# DATABASE CONNECTION
# ---------------------------------------

def get_db_connection():
    connection = sqlite3.connect("notes.db")
    connection.row_factory = sqlite3.Row
    return connection


# ---------------------------------------
# CREATE TABLE
# ---------------------------------------

connection = get_db_connection()

connection.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
""")

connection.commit()


# ---------------------------------------
# INSERT INITIAL NOTES
# ---------------------------------------

# Check whether the table is empty
count = connection.execute(
    "SELECT COUNT(*) FROM notes"
).fetchone()[0]

if count == 0:

    connection.execute("""
    INSERT INTO notes (title, content)
    VALUES (?, ?)
    """, ("Learn Flask", "Practice Flask REST API"))

    connection.execute("""
    INSERT INTO notes (title, content)
    VALUES (?, ?)
    """, ("Complete Internship", "Finish Flask tasks"))

    connection.commit()

connection.close()


# ---------------------------------------
# HOME
# ---------------------------------------

@app.route("/")
def home():

    connection = get_db_connection()

    notes = connection.execute(
        "SELECT * FROM notes"
    ).fetchall()

    connection.close()

    return jsonify([dict(note) for note in notes])


# ---------------------------------------
# GET ONE NOTE
# ---------------------------------------

@app.route("/notes/<int:id>", methods=["GET"])
def get_note(id):

    connection = get_db_connection()

    note = connection.execute("""
        SELECT * FROM notes
        WHERE id = ?
    """, (id,)).fetchone()

    connection.close()

    if note:
        return jsonify(dict(note))

    return jsonify({"error": "Note not found"}), 404


# ---------------------------------------
# POST - ADD NOTE
# ---------------------------------------

@app.route("/notes", methods=["POST"])
def add_note():

    data = request.get_json()

    title = data["title"]
    content = data["content"]

    connection = get_db_connection()

    cursor = connection.execute("""
        INSERT INTO notes (title, content)
        VALUES (?, ?)
    """, (title, content))

    connection.commit()

    new_id = cursor.lastrowid

    connection.close()

    new_note = {
        "id": new_id,
        "title": title,
        "content": content
    }

    return jsonify(new_note), 201


# ---------------------------------------
# PUT - UPDATE NOTE
# ---------------------------------------

@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):

    data = request.get_json()

    title = data["title"]
    content = data["content"]

    connection = get_db_connection()

    cursor = connection.execute("""
        UPDATE notes
        SET title = ?, content = ?
        WHERE id = ?
    """, (title, content, id))

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return jsonify({
            "error": "Note not found"
        }), 404

    connection.close()

    return jsonify({
        "id": id,
        "title": title,
        "content": content
    })


# ---------------------------------------
# DELETE - DELETE NOTE
# ---------------------------------------

@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):

    connection = get_db_connection()

    cursor = connection.execute("""
        DELETE FROM notes
        WHERE id = ?
    """, (id,))

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return jsonify({
            "error": "Note not found"
        }), 404

    connection.close()

    return jsonify({
        "message": "Note deleted successfully"
    })


# ---------------------------------------
# RUN FLASK
# ---------------------------------------

app.run(debug=True)