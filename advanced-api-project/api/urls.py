from django.urls import path
from api.views import AuthorView, ListView, CreateView, DeleteView, UpdateView, DetialView

urlpatterns = [
    """ API endpoints for the Book and Author resources """,
    
    path("authors/", AuthorView.as_view(), name="author"),
    path('books/', ListView.as_view(), name="list-book"),
    path('book/<int:pk>/', DetialView.as_view(), name="detail-view"),
    path("book/create/", CreateView.as_view(), name="create-book"),
    path('book/update/<int:pk>/', UpdateView.as_view(), name="update-book"),
    path('book/delete/<int:pk>/', DeleteView.as_view(), name="delete-book")
]
