# app/utils/token_helper.py
from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import timedelta

class TokenHelper:
    """
    Helper functions for managing JWT tokens.
    """

    @staticmethod
    def generate_access_token(identity, expires_delta=timedelta(days=1)):
        """
        Generate a new JWT access token.
        """
        return create_access_token(identity=identity, expires_delta=expires_delta)

    @staticmethod
    def get_current_identity():
        """
        Retrieve the identity from the current JWT token.
        """
        return get_jwt_identity()
