import pytest
from blog.models import Post, Category, Like
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from PIL import Image


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

@pytest.mark.django_db
def test_create_category(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post(
        "/api/categories/",
        {"name": "Python"},
        format='json'
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert Category.objects.count() == 1
    assert Category.objects.get().name == "Python"


@pytest.mark.django_db
def test_list_categories(api_client):
    Category.objects.create(name="Django")
    Category.objects.create(name="React")

    response = api_client.get("/api/categories/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

# added fixture for a blog test
@pytest.fixture 
@pytest.mark.django_db
def post(user):
    return Post.objects.create(title="A Test Post", content="Post content", author=user) # this creates a post and returns it

@pytest.mark.django_db
def test_like_post(api_client, user, post):
    api_client.force_authenticate(user=user)

    response = api_client.post(f"/api/posts/{post.pk}/like/")

    assert response.status_code == status.HTTP_201_CREATED
    assert Like.objects.count() == 1
    assert post.likes.count() == 1

@pytest.mark.django_db
def test_unlike_post(api_client, user, post):
    # first, create a like
    Like.objects.create(user=user, post=post)
    api_client.force_authenticate(user=user)

    # now, send another request to unlike it
    response = api_client.post(f"/api/posts/{post.pk}/like/")

    assert response.status_code == status.HTTP_200_OK
    assert post.likes.count() == 0

@pytest.mark.django_db
def test_update_user_profile_avatar(api_client, user):
    # authenticate the user
    api_client.force_authenticate(user=user)

    # Generate an in-memory image
    image_io = io.BytesIO()
    image = Image.new("RGB", (50, 50), color="red")  # small red square
    image.save(image_io, format="PNG")
    image_io.seek(0)

    dummy_image = SimpleUploadedFile(
        name="test_avatar.png",
        content=image_io.read(),
        content_type="image/png"
    )

    response = api_client.patch(
        "/api/auth/profile/",
        {"avatar": dummy_image},
        format="multipart"
    )

    print("DEBUG:", response.data)  # helpful to see exact API response if it still fails

    #assert the response and check if the avatar was updated
    assert response.status_code == 200

    # reload the user's profile from the database to check the update
    user.profile.refresh_from_db()

    # assert that the avatar field is no longer empty
    assert response.data["avatar"] is not None
    assert "/avatars/" in response.data["avatar"] # confirm file name is in the response URL
    assert user.profile.avatar.name.endswith(".png") # confirm the avatar field in the profile ends with the file name