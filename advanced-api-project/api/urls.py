from django.urls import path
from api.views import AuthorView, DetailView, ListView, CreateView, DeleteView, UpdateView

urlpatterns = [
    # /API endpoints for the Book and Author resources

    path("authors/", AuthorView.as_view(), name="author"),
    path('books/', ListView.as_view(), name="list-book"),
    path('books/<int:pk>/', DetailView.as_view(), name="detail-view"),
    path("books/create/", CreateView.as_view(), name="create-book"),
    path('books/update/<int:pk>/', UpdateView.as_view(), name="update-book"),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name="delete-book")
]
