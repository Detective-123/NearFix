from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/', views.logout, name='logout'),
]
