from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import CustomUser, Book
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

@permission_required("bookshelf.can_edit_books")
def list_books(request):
    books = Book.objects.all()
    if books is None:
        return HttpResponse("NO Books")
    return HttpResponse(str([book.title for book in books]))
