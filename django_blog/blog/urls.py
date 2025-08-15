from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from blog.views import (
    home, 
    register,
    ViewProfile,
    PostCreateView, 
    PostListView, 
    PostDetailView, 
    PostUpdateView,
    PostDeleteView
   )


urlpatterns = [
    path("auth/register/", register, name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ViewProfile.as_view(), name="profile"),
    path("post/new/", PostCreateView.as_view(), name="create_blog"),
    path("posts/", PostListView.as_view(), name="blogs"),
    path("home/", home, name="home"),
    path("post/<int:pk>/detail/", PostDetailView.as_view(), name="blog-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="update_blog"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_blog"),

]