from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from blog.views import register, ViewProfile, BlogCreateView, BlogListView
urlpatterns = [
    path("auth/register/", register, name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("me/", ViewProfile.as_view(), name="profile"),
    path("create/", BlogCreateView.as_view(), name="create_blog"),
    path("blogs/", BlogListView.as_view(), name="blogs")
]