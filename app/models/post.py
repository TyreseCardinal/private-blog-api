# app/models/post.py
from app import db

class Post(db.Model):
    """
    Post model for storing blog post information.
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """
        Convert post data to dictionary format for JSON responses.
        """
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }
