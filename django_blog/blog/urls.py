from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from blog.views import (
    home, 
    register,
    ProfileView,
    PostCreateView, 
    PostListView, 
    PostDetailView, 
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    ViewCommentsDetailView,
    CommentEditView,
    CommentDeleteView
   )


urlpatterns = [
    path("", home, name="home"),
    path("auth/register/", register, name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("post/new/", PostCreateView.as_view(), name="create_blog"),
    path("posts/", PostListView.as_view(), name="blogs"),
    path("post/<int:pk>/detail/", PostDetailView.as_view(), name="blog-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="update_blog"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_blog"),
    path("comment/<int:pk>/new/", CommentCreateView.as_view(), name="create_comment"),
    path("comment/<int:pk>/", ViewCommentsDetailView.as_view(), name="view_comments"),
    path("comment/<int:pk>/edit/", CommentEditView.as_view(), name="edit_comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete_comment")
    

]