from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Hello Flasumary_linesk!</h1>

    <h2>Home Page</h2>

    <a href="/about">About</a> |
    <a href="/contact">Contact</a>
    """


@app.route("/about")
def about():
    return """
    <h1>About Page</h1>

    <p>This is the About page of my flask application.</p>
    <p>This application is created using flask and python</P>


    <a href="/">Home</a> |
    <a href="/contact">Contact</a>
    """


@app.route("/contact")
def contact():
    return """
    
    
    <h1>Contact Page</h1>

    <p>This is the Contact page.</p>
    <p>Contact info:+91 9876543210</p>
    <p>email:pythonflask@gmail.com</p>

    <a href="/">Home</a> |
    <a href="/about">About</a>
    """


app.run(debug=True)