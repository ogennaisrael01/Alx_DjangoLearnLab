from django.urls import path
from api.views import AuthorView, BookVIew

urlpatterns = [
    path("author/", AuthorView.as_view(), name="author"),
    path('book/', BookVIew.as_view(), name="book")
]
