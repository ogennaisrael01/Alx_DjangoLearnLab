from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.conf import settings
from django.contrib.auth.models import User

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True, help_text="Required. Enter your Email")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def get_absloute_url(self):
        """ Returns a url of that user object """
        url = reverse("user-detail", args=[str(self.id)])
        return url
    
    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.username or self.email

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE, 
                               related_name="post")
    tag = models.ManyToManyField(Tag, related_name="post_tag", )
    
    def __str__(self):
        return self.title
    
    def get_absloute_url(self):
        """ Returns a url of that blog object """
        url = reverse("blog-detail", args=[str(self.id)])
        return url
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_comment")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content} by {self.author.username}: Post commented on {self.post.title}"

