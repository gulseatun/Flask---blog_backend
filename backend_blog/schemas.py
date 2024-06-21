from flask_marshmallow import Marshmallow
from models import User, Post, Comment

# Initialize Marshmallow instance
ma = Marshmallow()


class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing User model.
    """
    class Meta:
        model = User
        include_fk = True


class PostSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing Post model.
    """
    class Meta:
        model = Post
        include_fk = True


class CommentSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing Comment model.
    """
    class Meta:
        model = Comment
        include_fk = True
