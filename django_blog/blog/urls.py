from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from blog.views import (
    home, 
    register,
    ViewProfile,
    BlogCreateView, 
    BlogListView, 
    BlogDetailView, 
    BlogUpdateView,
    BlogDeleteView
   )


urlpatterns = [
    path("auth/register/", register, name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ViewProfile.as_view(), name="profile"),
    path("blog/create/", BlogCreateView.as_view(), name="create_blog"),
    path("blogs/", BlogListView.as_view(), name="blogs"),
    path("home/", home, name="home"),
    path("blog/detail/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blog/update/<int:pk>/", BlogUpdateView.as_view(), name="update_blog"),
    path("blog/delete/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),

]