import pytest
from django.contrib.auth.models import User
from rest_framework import status

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


@pytest.mark.django_db
def test_user_profile_creation(user):
    # the 'user' fixture creates a user, which should trigger the signal
    # ro create a corresponding profile, we test if it was created successfully
    assert hasattr(user, 'profile') # Check if profile attribute exists in user, if not, the test will fail here
    assert user.profile.user == user # Check if the profile's user is the same as the created user

@pytest.mark.django_db
def test_user_profile_update(api_client, user):
    api_client.force_authenticate(user=user) # Authenticate the client with the user

    #we send a patch request to update the user's bio. a patch request is used to update only the fields provided in the request
    response = api_client.patch(
        f"/api/auth/profile/",
        {"bio": "New bio for testing."},
        format='json'
    )

    user.profile.refresh_from_db() # refresh the user profile data from the database to get the latest changes.

    assert response.status_code == 200
    assert response.data["bio"] == "New bio for testing."
