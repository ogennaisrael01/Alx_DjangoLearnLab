from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookVIew(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer