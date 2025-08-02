from django.shortcuts import render
from api.models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get_queryset(self):
        """ Get a specific instance from the book model"""
        return super().get_queryset()

