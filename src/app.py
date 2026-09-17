# The main entry point to the app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# database I assume
db = SQLAlchemy()
login_manager = LoginManager()

def create_app() -> Flask:
    app = Flask(__name__)

    # Configuration - from .env??
    app.config["SECRET_KEY"] = os.environ.get(
            "SECRET_KEY",  "dev-only-insecure-key"
        )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "DATABASE_URL", "sqlite:///blog.db"
        )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    # routes.py
    from routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all() # Create tables if they don't exist ??

    return app

if __name__ == "__main__":
    app = create
    app.run(debug=True)
