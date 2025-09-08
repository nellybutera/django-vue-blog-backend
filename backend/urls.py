"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin # imports the admin module from django's contrib package. this module provides a built-in admin interface for managing the site's data.
from django.urls import path, include # path is used to define individual url patterns. include allows referencing other url configurations, making it easier to manage complex url structures.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)# import the JWT token obtain view for authentication endpoints
from users.views import ProfileUpdateView
from blog.views import CategoryListCreateView


urlpatterns = [ # this list holds all the url patterns for my project.
    path("admin/", admin.site.urls), # this line includes the default admin interface provided by django. it means that if i navigate to the /admin/ url of my site, i will be taken to the admin dashboard where i can manage my site's data.
    path("api/", include("blog.urls")), # this line includes all the urls defined in the blog app's urls.py file under the /api/ prefix. it means that any url starting with /blog/ will be handled by the url patterns defined in the blog app.
    path("api/auth/", include("users.urls")), # this line includes all the urls defined in the users app's urls.py file under the /api/auth/ prefix. it means that any url starting with /api/auth/ will be handled by the url patterns defined in the users app.
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"), # endpoint for obtaining JWT tokens, which means logging in and getting access and refresh tokens. which are useful for authenticating subsequent requests to protected endpoints (for logged-in users).
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # endpoint for refreshing JWT tokens, which means getting a new access token using a valid refresh token (for maintaining session without re-login).
    path("api/auth/profile/", ProfileUpdateView.as_view(), name='profile-update'), # endpoint for retrieving and updating the authenticated user's profile information. the name 'profile-update' can be used to reference this url pattern elsewhere in the project.
    path("api/categories/", CategoryListCreateView.as_view(), name="category-list-create"), # endpoint for listing all categories and creating new ones. it allows users to view existing categories and add new categories when they are logged in.

]
