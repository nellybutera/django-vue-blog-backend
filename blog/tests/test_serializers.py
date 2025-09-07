import pytest
from blog.models import Post
from blog.serializers import PostSerializer

@pytest.mark.django_db
def test_post_serializer(user): # Use the user fixture
    post = Post.objects.create(title="Serialized Post", content="Body", author=user)
    serializer = PostSerializer(post)
    data = serializer.data
    assert data["title"] == "Serialized Post"
    assert data["author"] == user.username