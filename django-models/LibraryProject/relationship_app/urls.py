from django.urls import path
from .views import all_books, LibraryDetailView
urlpatterns = [
    path("books/", all_books, name="books"),
    path("library_details", LibraryDetailView.as_view(), name="library_details")
]