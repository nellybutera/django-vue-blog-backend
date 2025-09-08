from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from blog.models import Profile

class RegisterView(generics.CreateAPIView): # createapi view is a generic view provided by drf that handles the creation of new model instances. it provides a simple way to create endpoints for user registration.
    queryset = User.objects.all() # retrieves all user objects from the database. while this isn't strictly necessary for a registration endpoint, it's included here as a standard practice.
    serializer_class = UserSerializer # points to the serializer that should be used for converting user instances to and from JSON. it tells the view how to serialize and deserialize the user data when sending responses or receiving requests.
    permission_classes = [permissions.AllowAny] # this means that any user, whether authenticated or not, can access this endpoint. it's important for registration endpoints, as new users won't have an account yet and need to be able to create one without any restrictions.


class ProfileUpdateView(generics.RetrieveUpdateAPIView): # retrieveupdateapi view is a generic view that provides GET and PUT/PATCH methods for retrieving and updating model instances. it's useful for allowing users to view and edit their own profiles.
    queryset = Profile.objects.all() # retrieves all profile objects from the database. similar to the register view, this is a standard practice, although in this case, the actual profile being accessed will be determined by the get_object method.
    serializer_class = ProfileSerializer # specifies the serializer to be used for profile data. it defines how profile instances are converted to and from JSON format.
    permission_classes = [permissions.IsAuthenticated] # this ensures that only authenticated users can access this endpoint. it's crucial for profile management, as users should only be able to view and edit their own profiles when they are logged in.

    def get_object(self): # this method is overridden to return the profile of the currently authenticated user. it ensures that users can only access their own profile data.
        return self.request.user.profile # accessing the profile attribute of the currently authenticated user (self.request.user). this assumes that there is a one-to-one relationship between the User model and the Profile model, allowing direct access to the user's profile.