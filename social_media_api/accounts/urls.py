from django.urls import path, include
from accounts import views

urlpatterns = [
    path("register/", views.RegistrationApiView.as_view(), name="register"),
    path("login/", views.LoginApiView.as_view(), name="login"),
]