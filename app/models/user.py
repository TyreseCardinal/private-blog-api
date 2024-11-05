# app/models/user.py
from datetime import datetime, timezone
from app import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    """
    User model for handling user information.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_picture = db.Column(db.String(300), nullable=True)  # Profile picture path
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def set_password(self, password):
        """
        Hashes and sets the password for the user.
        """
        self.password_hash = generate_password_hash(password).decode('utf-8')
    def check_password(self, password):
        """
        Checks if the provided password matches the stored hash.
        """
        return check_password_hash(self.password_hash, password)