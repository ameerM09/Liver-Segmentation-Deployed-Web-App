from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from os import path

db = SQLAlchemy()
DATABASE = "database.db"

def create_web_app():
    web_app = Flask(__name__)
    web_app.secret_key = "congressionalAppChallengeSubmission2024"

    # web_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE}"
    # db.init_app(web_app)

    from .routes import routes
    from .authentication import authentication

    web_app.register_blueprint(routes, url_prefix = "/")
    web_app.register_blueprint(authentication, url_prefix = "/")

    return web_app