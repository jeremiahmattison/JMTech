from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Register routes
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app