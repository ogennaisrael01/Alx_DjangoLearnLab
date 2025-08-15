from django.shortcuts import render
from rest_framework import generics
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer, BookInputSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters


"""
 A Basis CRUD API for Book and Author models using Django REST Framework.
 This API allows for creating, reading, updating, and deleting Book instances,
    as well as listing all authors and their associated books.

- permissions:
    - IsAuthenticatedOrReadOnly: Allows unauthenticated users to read data, but requires authentication for write operations.
    - IsAuthenticated: Requires the user to be authenticated for creating, updating, or deleting Book instances.
- serializers:
    - BookInputSerializer: Handles input validation and creation/updating of Book instances.
    - BookSerializer: Serializes Book instances for output.
    - AuthorSerializer: Serializes Author instances, including their associated books.
- filtering
    - django_filters: Provides filtering capabilities for listing books based on title, author, and publication year.
    - search: Allows searching for books by title and author.   
    - ordering: Enables ordering of books by publication year.

"""

class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["name", "books__title"]
    search_fields = ["name", "books__title"]  # Allows searching by author's name and associated book titles


class CreateView(generics.CreateAPIView):
    """ View to create a new Book instance. """
    # Using BookInputSerializer to handle input validation and creation
    queryset = Book.objects.all()
    serializer_class = BookInputSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """ Handle the creation of a new Book instance. """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
class ListView(generics.ListAPIView):
    """ View to list all Book instances. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allows unauthenticated users to view the 
    filter_backends = [rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["id", "title", "author", "publication_year"]
    ordering_fields = ["publication_year"]

    # def get_queryset(self):
    #     """ Override to filter books by the authenticated user. 
    #     Only books authored by the authenticated user will be returned.
    #     """
    #     return self.get_queryset()
        # user = Author.objects.get(name=self.request.user)
        # book = Book.objects.filter(author=user)
        # if book.exists():
        #     return book
        # return Response({f"message": "No Matching Query for you {self.request.user}"}, status=404)

class DetailView(generics.RetrieveAPIView):
    """ View to retrieve a single Book instance. """
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
   
class UpdateView(generics.UpdateAPIView):
    """ View to update an existing Book instance. """
    # Using BookInputSerializer to handle input validation and update
    queryset = Book.objects.all()
    serializer_class = BookInputSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    """ View to delete a Book instance. """
    queryset = Book.objects.all()
    serializer_class = BookInputSerializer
    permission_classes =[IsAuthenticated]