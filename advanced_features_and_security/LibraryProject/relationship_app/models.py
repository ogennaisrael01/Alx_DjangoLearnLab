from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model

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
    email = models.EmailField(unique=True, max_length=200, null=False, blank=False)
    password = models.CharField(max_length=50, name="password")
    date_of_birth = models.DateField(blank=True, null=True, max_length=200)
    profile_photo = models.ImageField(verbose_name="profile picture", blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200, default="First name", null=True, blank=True)
    last_name = models.CharField(max_length=200, default="Last name", null=True, blank=True)

    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.get_username()
    @property
    def is_staff(self):
        return self.is_admin

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, null=False)
    
    def __str__(self):
        return self.user.username
    
class Author(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authors")

    def __str__(self):
        return self.title, "by", self.author
    
    class Meta:
        permissions = (
            ("can_add_book", "can add book"),
            ("can_change_book", "can change book"),
            ("can_delete_book", "can delete book")
        )
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="library")
    
    def __str__(self):
        return self.name