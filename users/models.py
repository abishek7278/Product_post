from datetime import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    email=models.EmailField(max_length=264,unique=True)
    username=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=64)

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
