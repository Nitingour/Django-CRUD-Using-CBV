from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=255)
    price=models.FloatField()
    description=models.TextField()
    def get_absolute_url(self):
        return reverse('home')
