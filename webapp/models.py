# models.py
from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)  # Link resource to the faculty user
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')