from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView
urlpatterns = [
    path("books/", list_books, name="books"),
    path("library_details/", LibraryDetailView.as_view(), name="library_details"),
    path("register/", SignUpView.as_view(), name="register")
]