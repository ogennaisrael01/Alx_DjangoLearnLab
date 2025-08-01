from django.urls import path
from api.views import BookList, BookCreate


urlpatterns = [
    path("books/", BookList.as_view(), name="book-list"), # Maps to the book detail view
    path('create/book/', BookCreate.as_view(), name="create-book")
]