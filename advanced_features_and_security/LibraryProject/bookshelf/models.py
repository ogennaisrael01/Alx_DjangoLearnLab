from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **kwargs):
        if not email:
            return "Please provide your email address"
        normalize_email = self.normalize_email(email)
        user = self.model(email=normalize_email, password=password, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **kwargs):
        """ Method to create super user """

        user = self.create_user(email=email, password=password, **kwargs)
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
        


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True, max_length=200)
    profile_photo = models.ImageField(verbose_name="profile picture", blank=True, null=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f'{self.title} {self.author}'