from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize SQLAlchemy instance
db = SQLAlchemy()
DB_NAME = "app.db"


def create_app():

    """
    Creates and configures the Flask application.

    Returns:
        app: The Flask application instance.
    """

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cdefghjklm'

    # Configure the database URI for SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    # Disable track modifications to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy database with the Flask application
    db.init_app(app)

    # Create the database if it doesn't exist
    create_database(app)
    return app


def create_database(app):
    """
    Creates the database if it does not exist.

    Args:
        app: The Flask application instance.
    """

    # Use the application context to perform database operations
    with app.app_context():
        # Check if the database file exists
        if not path.exists("backend_blog/" + DB_NAME):
            # Create all database tables based on defined models
            db.create_all()
