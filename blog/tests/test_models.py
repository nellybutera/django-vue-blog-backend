import pytest
from django.contrib.auth.models import User
from blog.models import Post, Comment

@pytest.mark.django_db
def test_create_post():
    user = User.objects.create_user(username="testuser", password="pass123")
    post = Post.objects.create(title="Test Post", content="Some content", author=user)
    assert post.title == "Test Post"
    assert post.author.username == "testuser"

@pytest.mark.django_db
def test_create_comment():
    user = User.objects.create_user(username="testuser", password="pass123")
    post = Post.objects.create(title="Test Post", content="Some content", author=user)
    comment = Comment.objects.create(post=post, author=user, content="Nice!")
    assert comment.content == "Nice!"
    assert comment.post == post
