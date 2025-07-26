from django.urls import path
from . import views
urlpatterns = [
    path("book/", views.list_books, name="books")
]