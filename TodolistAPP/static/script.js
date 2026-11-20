async function addNote() {

    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    if (title === "" || content === "") {
        alert("Please enter title and content");
        return;
    }

    const response = await fetch("/notes", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            title: title,
            content: content
        })
    });

    const result = await response.json();

    alert(result.message);

    document.getElementById("title").value = "";
    document.getElementById("content").value = "";

    loadNotes();
}


async function loadNotes() {

    const response = await fetch("/notes");

    const notes = await response.json();

    const container = document.getElementById("notesContainer");

    container.innerHTML = "";

    notes.forEach(note => {

        const div = document.createElement("div");

        div.className = "note";

        div.innerHTML = `
            <h3>${note.title}</h3>
            <p>${note.content}</p>

            <button onclick="deleteNote(${note.id})">
                Delete
            </button>
        `;

        container.appendChild(div);
    });
}


async function deleteNote(id) {

    await fetch(`/notes/${id}`, {
        method: "DELETE"
    });

    loadNotes();
}


loadNotes();