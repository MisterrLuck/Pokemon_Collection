# The main entry point to the app
# url_for is for the function

from flask import Flask, request, render_template, make_response, redirect, abort, url_for
import os
from database import db_session

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def hello_world():
    return redirect(url_for("login"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/new", methods=["GET", "POST"])
def new_card():
    return render_template("new_card.html")

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", person=name)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    # Submitted login details
    if request.method == "POST":
        user = request.form["username"]
        if user in ["Lizzy", "Josh", "Victoria"]:
            # I want to change this to use url_for or smth
            temp = render_template("hello.html", username=user)
            return temp
        else:
            error = "Invalid username"

    # launches login if GET method or if error
    return render_template("login.html", error=error)

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["the_file"]
        f.save("/var/www/images/uploaded_image.png")

