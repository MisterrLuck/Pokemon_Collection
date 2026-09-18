# The main entry point to the app

from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello World!</p><a href=\"hello_func\">Link</a>"

@app.route("/hello")
@app.route("/hello/<name>")
def hello_func(name=None):
    return render_template("test.html", person=name)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    user_cookie = request.cookies.get("username")

    # Submitted login details
    if request.method == "POST" or user_cookie:
        user = user_cookie if user_cookie else request.form["username"]
        if user in ["Lizzy", "Josh"]:
            temp = render_template("test.html", username=user)
            resp = make_response(temp)
            resp.set_cookie("username", user)
            return resp
        else:
            error = "Invalid username"

    # launches login if GET method or if error
    return render_template("login.html", error=error)

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["the_file"]
        f.save("/var/www/images/uploaded_image.png")

# database I assume
#db = SQLAlchemy()
#login_manager = LoginManager()

#def create_app() -> Flask:
#    app = Flask(__name__)
#
#    # Configuration - from .env??
#    app.config["SECRET_KEY"] = os.environ.get(
#            "SECRET_KEY",  "dev-only-insecure-key"
#        )
#    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
#            "DATABASE_URL", "sqlite:///blog.db"
#        )
#    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
#    db.init_app(app)
#    login_manager.init_app(app)
#    login_manager.login_view = "main.login"
#
#    # routes.py
#    from routes import main
#    app.register_blueprint(main)
#
#    with app.app_context():
#        db.create_all() # Create tables if they don't exist ??
#
#    return app
#
#if __name__ == "__main__":
#    app = create
#    app.run(debug=True)
