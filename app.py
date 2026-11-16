from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    items = ["Bracelet", "Necklace", "Earrings", "Ring"]

    return render_template(
        "landingpage.html",
        name="Karunya",
        items=items
    )


@app.route("/user/<name>")
def user(name):
    items = ["Bracelet", "Necklace", "Earrings", "Ring"]

    return render_template(
        "landingpage.html",
        name=name,
        items=items
    )


if __name__ == "__main__":
    app.run(debug=True)