from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.login, name="login")
=======
    path("", views.home, name="home"),
    path("/login", views.login, name="login")
>>>>>>> 3d52695e3ce24c9314b333393aba7a3b5a4628a1
]
