from flask_sqlalchemy import SQLAlchemy
from __init__ import db


class User(db.Model):
    """
    Defines the User model.

    Attributes:
        id (int): Primary key.
        name (str): User's name.
        email (str): User's email.
        job (str): User's job.
        posts (relationship): Relationship to the Post model.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    job = db.Column(db.String(50))
    posts = db.relationship('Post', backref='author', lazy=True)


class Post(db.Model):
    """
    Defines the Post model.

    Attributes:
        id (int): Primary key.
        title (str): Title of the post.
        description (str): Description of the post.
        user_id (int): Foreign key to the User model.
        comments (relationship): Relationship to the Comment model.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)


class Comment(db.Model):
    """
    Defines the Comment model.

    Attributes:
        id (int): Primary key.
        content (str): Content of the comment.
        post_id (int): Foreign key to the Post model.
    """
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
