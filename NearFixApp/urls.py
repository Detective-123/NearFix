from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.index, name="index"),

    # AUTH
    path("login", views.login, name="login")
=======
    path("", views.home, name="index")
>>>>>>> 2ff8f80a243a6b97ee6899930bff1bc40ecd0eee
]
