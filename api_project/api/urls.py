from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken import views
routers = DefaultRouter()
routers.register("book_list", BookViewSet, basename="book_list")

# include all URL for the BookViewSet (CRUD)
urlpatterns = [
    path("", include(routers.urls)),
    path("obtain-auth-token/", views.obtain_auth_token, name="auth-token")
]