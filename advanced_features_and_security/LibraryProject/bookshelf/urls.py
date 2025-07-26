from django.urls import path
from . import views
urlpatterns = [
    path("book/", views.book_list, name="books"),
    path("register/", views.register, name="register")
]