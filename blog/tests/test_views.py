import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from blog.models import Post

@pytest.mark.django_db
def test_list_posts():
    user = User.objects.create_user(username="testuser", password="pass123")
    Post.objects.create(title="API Post", content="Hello world", author=user)
    client = APIClient()
    response = client.get("/api/posts/")
    assert response.status_code == 200
    assert response.data[0]["title"] == "API Post"

@pytest.mark.django_db
def test_create_post_authenticated():
    user = User.objects.create_user(username="testuser", password="pass123")
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post("/api/posts/", {"title": "New Post", "content": "Body"})
    assert response.status_code == 201
    assert response.data["title"] == "New Post"
