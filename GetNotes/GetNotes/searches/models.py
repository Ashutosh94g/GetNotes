from django.db import models

# Create your models here.
class SeachQuary(models.Model):
    query = models.CharField(max_length = 220)
    timestamp = models.DateTimeField(auto_now_add=True)