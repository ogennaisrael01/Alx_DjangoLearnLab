from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.conf import settings
from django.urls import reverse


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    bio = models.TextField()
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following", symmetrical=False)
    profile_picture = models.ImageField(upload_to="user_profile", blank=True, null= True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def __str__(self):
        """ string reprensatation on the user object"""
        return self.get_full_name()
    
    def get_absolute_url(self):
        """ return an absolute URL to refrence this user"""
        return reverse("user-detail", args=str(self["id"]))
    
