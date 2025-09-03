from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView): # createapi view is a generic view provided by drf that handles the creation of new model instances. it provides a simple way to create endpoints for user registration.
    queryset = User.objects.all() # retrieves all user objects from the database. while this isn't strictly necessary for a registration endpoint, it's included here as a standard practice.
    serializer_class = UserSerializer # points to the serializer that should be used for converting user instances to and from JSON. it tells the view how to serialize and deserialize the user data when sending responses or receiving requests.
    permission_classes = [permissions.AllowAny] # this means that any user, whether authenticated or not, can access this endpoint. it's important for registration endpoints, as new users won't have an account yet and need to be able to create one without any restrictions.