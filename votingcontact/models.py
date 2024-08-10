from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
   
    




