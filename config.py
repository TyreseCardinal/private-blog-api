# config.py
import os
from dotenv import load_dotenv  # Requires `python-dotenv` package

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Base configuration with common settings"""
    
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24).hex())
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_default_jwt_secret')  # Replace in production

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/private-blog'
    SQLALCHEMY_ECHO = True  # Enables logging of SQL statements

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:password@localhost/private-blog')
    SQLALCHEMY_ECHO = False  # Turn off SQL logging in production

# Configuration dictionary for easily retrieving settings
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
