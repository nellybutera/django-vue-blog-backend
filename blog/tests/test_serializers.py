import pytest
from django.contrib.auth.models import User
from blog.models import Post
from blog.serializers import PostSerializer

@pytest.mark.django_db
def test_post_serializer():
    user = User.objects.create_user(username="testuser", password="pass123")
    post = Post.objects.create(title="Serialized Post", content="Body", author=user)
    serializer = PostSerializer(post)
    data = serializer.data
    assert data["title"] == "Serialized Post"
    assert data["author"] == "testuser"
