from django.db import models

class Vote(models.Model):
    
    candidate = models.CharField(max_length=20)