# This is where i will have all my logic for web requests and responses. 
# Including everything in between. All functionalities will be defined here.

from rest_framework import viewsets, permissions , generics # imports viewsets and permissions modules from the Django rest_framework package. viewsets provide a way to define the behavior of my api endpoints, while permissions help control access to those endpoints based on user authentication and authorization. generics provides generic views that can be used to quickly create common api views.
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

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


class RegisterView(generics.CreateAPIView): # createapi view is a generic view provided by drf that handles the creation of new model instances. it provides a simple way to create endpoints for user registration.
    queryset = User.objects.all() # retrieves all user objects from the database. while this isn't strictly necessary for a registration endpoint, it's included here as a standard practice.
    serializer_class = UserSerializer # points to the serializer that should be used for converting user instances to and from JSON. it tells the view how to serialize and deserialize the user data when sending responses or receiving requests.
    permission_classes = [permissions.AllowAny] # this means that any user, whether authenticated or not, can access this endpoint. it's important for registration endpoints, as new users won't have an account yet and need to be able to create one without any restrictions.