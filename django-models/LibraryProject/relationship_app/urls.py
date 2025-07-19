from django.urls import path
from . import views
urlpatterns = [
    path("books/", views.all_books, name="books"),
    path("library_details", views.LibraryDetail.as_view(), name="library_details")
]