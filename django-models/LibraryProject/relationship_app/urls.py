from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("books/", views.list_books, name="books"),
    path("library_details/", views.LibraryDetailView.as_view(), name="library_details"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("admin_view/", views.admin_view, name="admin_view"),
    path("librarian_view/", views.librarian_view, name="librarian_view"),
    path("member_view/", views.member_view, name="member_view")
]