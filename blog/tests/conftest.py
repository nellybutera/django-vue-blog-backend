import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.fixture
def user():
    """A fixture to create and return a new User instance."""
    return User.objects.create_user(username="testuser", password="pass123")

@pytest.fixture
def api_client():
    """A fixture to return a new APIClient instance."""
    return APIClient()