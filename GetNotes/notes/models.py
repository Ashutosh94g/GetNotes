from django.db import models

# Create your models here.

class Notes(models.Model):
	"""docstring for Notes
	1. define department, subject, slug
	"""
	department = models.CharField(max_length = 64)
	subject = models.CharField(max_length = 64)
	slug = models.SlugField()