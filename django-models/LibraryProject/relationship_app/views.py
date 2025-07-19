from django.shortcuts import render, redirect
from.models import  Book
from .models import Library, UserProfile
from django.views.generic import DetailView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {
        "books":books
    })

class LibraryDetailView(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {
        "form":form
    })

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

@user_passes_test
def admin_view(request):
    return  render(request, "relationship_app/admin_view.html")

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

@user_passes_test
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"
@user_passes_test
def member_view(request):
    return render(request, "relationship_app/member_view.html")