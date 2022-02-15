from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=128)
    weight_in_kgs=models.IntegerField(max_length=10)
    price_in_rupees=models.IntegerField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)