from django.shortcuts import render
from rest_framework import generics
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer, BookInputSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly] # Allows unauthenticated users to view the list 

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