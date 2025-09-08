import pytest
from blog.models import Post, Comment

@pytest.mark.django_db
def test_create_post(user): # Use the user fixture
    post = Post.objects.create(title="Test Post", content="Some content", author=user)
    assert post.title == "Test Post"
    assert post.author.username == "testuser"

@pytest.mark.django_db
def test_create_comment(user): # Use the user fixture
    post = Post.objects.create(title="Test Post", content="Some content", author=user)
    comment = Comment.objects.create(post=post, author=user, content="Nice!")
    assert comment.content == "Nice!"
    assert comment.post == post

