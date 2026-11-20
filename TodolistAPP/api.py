from flask import Flask, request, jsonify, render_template
import database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes", methods=["GET"])
def get_notes():

    notes = database.get_notes()

    return jsonify(notes)        


# POST - Add note
@app.route("/notes", methods=["POST"])
def add_note():

    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({
            "error": "Title and content are required"
        }), 400

    note_id = database.add_note(title, content)

    return jsonify({
        "message": "Note added successfully",
        "id": note_id
    }), 201


@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):

    data = request.get_json()

    title = data.get("title")
    content = data.get("content")
    completed = data.get("completed", 0)

    database.update_note(
        note_id,
        title,
        content,
        completed
    )

    return jsonify({
        "message": "Note updated successfully"
    })

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):

    database.delete_note(note_id)

    return jsonify({
        "message": "Note deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)