from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager

# Create your models here.
class userprofile(models.Model):
  phone=models.CharField(max_length=10, unique=True)
  full_name=models.CharField(max_length=20,unique=False)
  email=models.EmailField()
  created_at = models.DateTimeField(auto_now_add=True)
  

def __str__(self):
    return f"{self.phone} - {self.full_name}"
