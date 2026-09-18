# The main entry point to the app

from flask import Flask, request, render_template, make_response
import os
from database import db_session

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def hello_world():
    return render_template("base.html")

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("test.html", person=name)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    #user_cookie = request.cookies.get("username")

    # Submitted login details
    if request.method == "POST": # or user_cookie:
        #user = user_cookie if user_cookie else request.form["username"]
        user = request.form["username"]
        if user in ["Lizzy", "Josh"]:
            temp = render_template("test.html", username=user)
            #resp = make_response(temp)
            #resp.set_cookie("username", user)
            #return resp
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

