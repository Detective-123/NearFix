from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
<<<<<<< HEAD
def index(request):
  return render(request, "index.html")

def login(request):
  return render(request, "login.html")

def register(request):
  return render(request, "register.html")
=======
def home(request):
  return render(request, "home.html")
>>>>>>> 2ff8f80a243a6b97ee6899930bff1bc40ecd0eee
