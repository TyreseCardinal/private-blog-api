# app/services/auth_service.py
from app.models.user import User
from app import db, bcrypt
from app.utils.token_helper import TokenHelper

class AuthService:
    """
    Service class for handling authentication logic.
    """

    @staticmethod
    def register_user(username, email, password):
        """
        Register a new user and hash their password.
        """
        if User.query.filter((User.username == username) | (User.email == email)).first():
            return {"error": "Username or email already exists"}, 400

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

    @staticmethod
    def authenticate_user(username, password):
        """
        Authenticate user credentials and return an access token if valid.
        """
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = TokenHelper.generate_access_token({"username": username})
            return {"access_token": access_token}, 200
        return {"error": "Invalid credentials"}, 401
