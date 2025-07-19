"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView as auth_login
from django.contrib.auth.views import LogoutView as auth_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("relationship_app.urls")),
    path("login/", auth_login.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_logout.as_view(template_name="relationship/logout.html"), name="logout")
]
