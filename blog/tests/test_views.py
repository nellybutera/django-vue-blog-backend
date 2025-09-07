import pytest
from blog.models import Post

@pytest.mark.django_db
def test_list_posts(api_client, user): # Use the api_client and user fixtures
    Post.objects.create(title="API Post", content="Hello world", author=user)
    response = api_client.get("/api/posts/")
    assert response.status_code == 200
    assert response.data[0]["title"] == "API Post"

@pytest.mark.django_db
def test_create_post_authenticated(api_client, user): # Use the fixtures
    api_client.force_authenticate(user=user)
    response = api_client.post("/api/posts/", {"title": "New Post", "content": "Body"})
    assert response.status_code == 201
    assert response.data["title"] == "New Post"