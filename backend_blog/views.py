from flask import request
from flask_marshmallow import Marshmallow
from models import User, Post, Comment
from __init__ import db
from schemas import UserSchema, PostSchema, CommentSchema
from __init__ import create_app

# Create and configure the Flask application
app = create_app()
# Initialize Marshmallow with the Flask app
ma = Marshmallow(app)

# Schemas for serializing and deserializing models
user_schema = UserSchema()
users_schema = UserSchema(many=True)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


@app.route('/user', methods=['POST'])
def add_users():
    """
    Adds one or more users.

    Returns:
        json: JSON representation of the added users.
    """
    users = request.json
    new_users = []

    for user in users:
        name = user['name']
        email = user['email']
        job = user['job']
        new_user = User(name=name, email=email, job=job)
        new_users.append(new_user)
        db.session.add(new_user)

    db.session.commit()
    return users_schema.jsonify(new_users)


@app.route('/users', methods=['GET'])
def get_users():
    """
    Returns all users.

    Returns:
        json: JSON representation of all users.
    """
    users = User.query.all()
    return users_schema.jsonify(users)


@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    """
    Updates a specific user's information.

    Args:
        id (int): The ID of the user to update.

    Returns:
        json: JSON representation of the updated user.
    """
    user = User.query.get(id)
    user.name = request.json['name']
    user.email = request.json['email']
    user.job = request.json['job']
    db.session.commit()
    return user_schema.jsonify(user)


@app.route('/post', methods=['POST'])
def add_post():
    """
    Adds a new post for a specific user.

    Returns:
        json: JSON representation of the added post.
    """
    title = request.json['title']
    description = request.json['description']
    user_id = request.json['user_id']
    new_post = Post(title=title, description=description, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return post_schema.jsonify(new_post)


@app.route('/user/<id>/posts', methods=['GET'])
def get_user_posts(id):
    """
    Returns all posts for a specific user.

    Args:
        id (int): The ID of the user.

    Returns:
        json: JSON representation of the user's posts.
    """
    posts = Post.query.filter_by(user_id=id).all()
    return posts_schema.jsonify(posts)


@app.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
    """
    Deletes a specific post.

    Args:
        id (int): The ID of the post to delete.

    Returns:
        json: JSON representation of the deleted post.
    """
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return post_schema.jsonify(post)


@app.route('/comment', methods=['POST'])
def add_comment():
    """
    Adds a comment to a specific post.

    Returns:
        json: JSON representation of the added comment.
    """
    content = request.json['content']
    post_id = request.json['post_id']
    new_comment = Comment(content=content, post_id=post_id)
    db.session.add(new_comment)
    db.session.commit()
    return comment_schema.jsonify(new_comment)


@app.route('/post/<id>/comments', methods=['GET'])
def get_post_comments(id):
    """
    Returns all comments for a specific post.

    Args:
        id (int): The ID of the post.

    Returns:
        json: JSON representation of the post's comments.
    """
    comments = Comment.query.filter_by(post_id=id).all()
    return comments_schema.jsonify(comments)
