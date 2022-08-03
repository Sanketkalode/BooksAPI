"""Flask app module to create and initalize flask app"""
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from app.controller import views
from app.controller.author import auth_blueprint
from app.controller.books import book_blueprint
from app.controller.user import user_blueprint

db = MongoEngine()
jwt = JWTManager()


def create_app(config):
    """Function to create flask app"""
    app = Flask(__name__)
    app.config.from_object(config)

    add_extensions(app)
    add_blueprints(app)

    return app


def add_extensions(app):
    """Initialization of flask extensions"""

    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resource={r"/": {"origins": "*"}})


def add_blueprints(app):
    """Registration of blueprints"""

    app.register_blueprint(views)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(book_blueprint)
    app.register_blueprint(user_blueprint)
