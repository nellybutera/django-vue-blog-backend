# This is where i will have all my logic for web requests and responses. 
# Including everything in between. All functionalities will be defined here.

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet): # modelviewset provides default implementations for standard actions like list, create, retrieve, update, and destroy. it is a class provided by drf that simplifies the process of creating api endpoints for my models.
    queryset = Post.objects.all().order_by("-created_at") # retrieves all post objects from the database and orders them by created_at in descending order (newest first). it's a database query that defines which set of data this viewset will operate on. the hyphen (-) before created_at indicates descending order.
    serializer_class = PostSerializer # points to the serializer that should be used for converting post instances to and from JSON. it tells the viewset how to serialize and deserialize the post data when sending responses or receiving requests.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # this means that any user can view the posts (read-only access), but only authenticated users can create, update, or delete posts. it helps secure the api by restricting certain actions to logged-in users only. it's a built-in permission class provided by drf.

    def perform_create(self, serializer): # this method is overridden to customize the behavior when a new post is created. it allows us to set additional attributes on the post instance before it's saved to the database.
        serializer.save(author=self.request.user) # when a new post is created, this line automatically sets the author field of the post to the currently authenticated user (self.request.user). this ensures that the post is associated with the user who created it, without requiring the client to explicitly provide the author information in the request.


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
