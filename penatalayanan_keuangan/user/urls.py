from django.contrib import admin
from django.urls import path
from . import views

# from django.contrib.auth import views as authentication_views

app_name = "user"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # path("forum/", views.forum, name="forum"),
]
