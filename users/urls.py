from django.urls import path
from .views import RegisterView

urlpatterns = [
       path("register/", RegisterView.as_view(), name="register"), # this line defines a url pattern for user registration. it means that if i navigate to the "register/" url of the blog app, i will be taken to the RegisterView, which handles user registration. the name argument allows me to refer to this url pattern by name in other parts of my code.
]
