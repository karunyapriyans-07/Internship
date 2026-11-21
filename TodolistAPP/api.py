from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

import database

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/")
def home():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "index.html",
        username=session["username"]
    )

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Username and password are required"

        hashed_password = generate_password_hash(password)

        user_id = database.add_user(
            username,
            hashed_password
        )

        if user_id is None:
            return "Username already exists"

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = database.get_user(username)

        if user and check_password_hash(
            user["password"],
            password
        ):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("home"))

        return "Invalid username or password"

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

@app.route("/notes", methods=["GET"])
def get_notes():

    if "user_id" not in session:
        return jsonify({
            "error": "Please login first"
        }), 401

    notes = database.get_notes(
        session["user_id"]
    )

    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():

    if "user_id" not in session:
        return jsonify({
            "error": "Please login first"
        }), 401

    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({
            "error": "Title and content are required"
        }), 400

    note_id = database.add_note(
        title,
        content,
        session["user_id"]
    )

    return jsonify({
        "message": "Note added successfully",
        "id": note_id
    }), 201

@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):

    if "user_id" not in session:
        return jsonify({
            "error": "Please login first"
        }), 401

    data = request.get_json()

    title = data.get("title")
    content = data.get("content")
    completed = data.get("completed", 0)

    database.update_note(
        note_id,
        title,
        content,
        completed,
        session["user_id"]
    )

    return jsonify({
        "message": "Note updated successfully"
    })

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):

    if "user_id" not in session:
        return jsonify({
            "error": "Please login first"
        }), 401

    database.delete_note(
        note_id,
        session["user_id"]
    )

    return jsonify({
        "message": "Note deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)