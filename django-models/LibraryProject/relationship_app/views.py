from django.shortcuts import render
from.models import Author, Book, Library, Librarian
from django.views.generic import ListView
# Create your views here.

def all_books(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {
        "books":books
    })

class LibraryDetail(ListView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
