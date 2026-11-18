from flask import Flask, request, jsonify

app = Flask(__name__)

notes = [
    {
        "id": 1,
        "title": "Learn Flask",
        "content": "Practice Flask REST API"
    },
    {
        "id": 2,
        "title": "Complete Internship",
        "content": "Finish Flask tasks"
    }
]
@app.route("/")
def home():
    return jsonify(notes)
  


    


@app.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    for note in notes:
        if note["id"] == id:
            return jsonify(note)

    return jsonify({"error": "Note not found"}), 404


# POST - Add a new note
@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()

    new_note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"]
    }

    notes.append(new_note)

    return jsonify(new_note), 201


@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):
    data = request.get_json()

    for note in notes:
        if note["id"] == id:
            note["title"] = data["title"]
            note["content"] = data["content"]

            return jsonify(note)

    return jsonify({"error": "Note not found"}), 404


@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    for note in notes:
        if note["id"] == id:
            notes.remove(note)

            return jsonify({
                "message": "Note deleted successfully"
            })

    return jsonify({"error": "Note not found"}), 404


app.run(debug=True)