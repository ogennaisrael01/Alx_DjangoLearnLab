from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import CustomUser, Book
from django.http import  HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import ExampleForm
from django.views import generic
from rest_framework import request, response

# Create your views here.

@permission_required("bookshelf.can_edit_books", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    if books is None:
        return HttpResponse("NO Books")
    return render(request, "bookshelf/book_list.html", context={"books": books})

def register(request):
    try:
        if request.method == "POST":
            form  = ExampleForm(request.POST)
            if form.is_valid() and form.validate_password(form.cleaned_data["password"]):
                form.save()
                return redirect("books")
        else:
            form = ExampleForm()

    except ExampleForm.errors as e:
        return f"Error {e}"
    return render(request, "bookshelf/register.html", context={"form": form})

