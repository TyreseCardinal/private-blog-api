# app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import config

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name):
    """
    Application factory function. Configures app settings and initializes extensions.
    
    Args:
        config_name (str): The name of the configuration to use ('development' or 'production').
    
    Returns:
        Flask app instance configured with the specified settings.
    """
    app = Flask(__name__)
    CORS(app)
    # Load the specified configuration from the config object
    app.config.from_object(config[config_name])

    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints for authentication, posts, and user management
    from .routes import auth_bp, post_bp, user_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(post_bp, url_prefix='/posts')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
