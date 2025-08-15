from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.conf import settings
from django.contrib.auth.models import User

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True, help_text="Required. Enter your Email")
    creates_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE, 
                               related_name="post")
    