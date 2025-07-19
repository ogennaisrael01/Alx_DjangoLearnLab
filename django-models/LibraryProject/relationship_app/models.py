from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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