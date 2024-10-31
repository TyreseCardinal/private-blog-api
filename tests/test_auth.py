# tests/test_auth.py

import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def client():
    """
    Set up a test client and initialize a fresh database before each test.
    """
    app = create_app('testing')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Temporary in-memory database for testing

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register(client):
    """
    Test user registration endpoint.
    """
    response = client.post('/auth/register', json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 201
    assert response.json['message'] == "User registered successfully"

def test_login(client):
    """
    Test user login endpoint and check token generation.
    """
    # First, register a user
    client.post('/auth/register', json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    })

    # Attempt to log in with the same credentials
    response = client.post('/auth/login', json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_protected_route(client):
    """
    Test accessing a protected route with and without a token.
    """
    # First, register and log in a user to get a token
    client.post('/auth/register', json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    })
    login_response = client.post('/auth/login', json={
        "username": "testuser",
        "password": "testpassword"
    })
    access_token = login_response.json['access_token']

    # Access protected route without token
    response = client.get('/posts/')
    assert response.status_code == 401  # Unauthorized

    # Access protected route with token
    response = client.get('/posts/', headers={
        "Authorization": f"Bearer {access_token}"
    })
    assert response.status_code == 200  # OK
