# this file is for defining my data models, meaning python classes which are my database tables.
# It will contain all the models for my blogs and their fields.

from django.db import models # importing models module form django's database library.
from django.contrib.auth.models import User #Django's built-in user model

from django.db.models.signals import post_save # to create a user profile automatically when a new user is created.
from django.dispatch import receiver # to listen for the post_save signal.

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
    

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    

@receiver(post_save, sender=User) # signal receiver function to create a profile when a new user is created.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs): # this function saves the profile whenever the user is saved.
    instance.profile.save() # save the profile whenever the user is saved.