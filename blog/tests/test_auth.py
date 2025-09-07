import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_registration(api_client): # Use the api_client fixture
    response = api_client.post("/api/auth/register/", {
        "username": "newuser",
        "password": "securepass",
        "email": "newuser@example.com"
    })
    assert response.status_code == 201
    assert response.data["username"] == "newuser"

@pytest.mark.django_db
def test_jwt_login(api_client, user): # Use the api_client and user fixtures
    # The 'user' fixture automatically creates the user, no need to do it here
    response = api_client.post("/api/auth/token/", {
        "username": user.username,
        "password": "pass123"
    })
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data