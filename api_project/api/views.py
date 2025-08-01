from django.shortcuts import render
from api.models import Book
from api.serializers import BookSerializer
from rest_framework import generics

# Create your views here.

class BookCreate(generics.CreateAPIView):
    queryset = Book
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
        
    

class BookList(generics.ListAPIView):
    queryset = Book
    serializer_class = BookSerializer

    def get_queryset(self):
        return self.queryset.objects.all()