from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")


@app.route("/")
def home():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return render_template("thankyou.html", name=name)


app.run(debug=True)