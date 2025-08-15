from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    """ Represents an author in the system. """
    name = models.CharField(max_length=100)

    def __str__(self):
        """ Returns the string representation of the author. """
        return self.name

class Book(models.Model):
    """ Represents a book in the system. """
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books") # ForeignKey to Author model
    publication_year = models.IntegerField() # Year the book was published

    def __str__(self):
        """ Returns the string representation of the book. """
        return f"{self.title} by {self.author.name}"
    def get_absolute_url(self):
        return reverse("detail-view", args=[str(self.id)])

