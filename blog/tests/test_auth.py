import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    response = client.post("/api/auth/register/", {
        "username": "newuser",
        "password": "securepass",
        "email": "newuser@example.com"
    })
    assert response.status_code == 201
    assert response.data["username"] == "newuser"

@pytest.mark.django_db
def test_jwt_login():
    user = User.objects.create_user(username="jwtuser", password="securepass")
    client = APIClient()
    response = client.post("/api/auth/token/", {
        "username": "jwtuser",
        "password": "securepass"
    })
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
