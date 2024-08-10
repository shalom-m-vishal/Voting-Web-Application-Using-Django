from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class loginForm(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)