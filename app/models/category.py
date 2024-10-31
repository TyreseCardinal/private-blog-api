# app/models/category.py
from app import db

class Category(db.Model):
    """
    Category model for organizing posts by category.
    """
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        """
        Convert category data to dictionary format.
        """
        return {
            'id': self.id,
            'name': self.name
        }
