from django.shortcuts import render
from api.models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset.objects.all()

