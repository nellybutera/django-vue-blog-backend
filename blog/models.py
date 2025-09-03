# this file is for defining my data models, meaning python classes which are my database tables.
# It will contain all the models for my blogs and their fields.

from django.db import models # importing models module form django's database library.
from django.contrib.auth.models import User #Django's built-in user model

# django creates a new table called Post.
class Post(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # string representation of the model, it helps to identify the object easily when we print it.
        return self.title

# this defines a comment database table  
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") # foreign relating comments to a single post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments") # linking comments to user, all allows us to get all comments made by the user.
    content = models.TextField() # stores comment's text
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # human readable representation of the comment object
        return f"Comment by {self.author.username} on {self.post.title}"
    