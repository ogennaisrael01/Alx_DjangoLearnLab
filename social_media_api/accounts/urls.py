from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserApiView)

urlpatterns = [
    path('', include(router.urls)),
    path("register/", views.RegistrationApiView.as_view(), name="register"),
    path("login/", views.LoginApiView.as_view(), name="login"),
]