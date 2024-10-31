# app/routes/post_routes.py
from flask import Blueprint, request, jsonify
from app.models.post import Post
from app import db
from flask_jwt_extended import jwt_required

post_bp = Blueprint('post', __name__)

@post_bp.route('/', methods=['GET'])
@jwt_required()
def get_posts():
    """
    Retrieve all posts. User must be authenticated.
    """
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200

@post_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    """
    Create a new post with a title and content.
    """
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "Post created successfully"}), 201
