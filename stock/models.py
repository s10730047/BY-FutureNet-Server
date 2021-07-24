from django.db import models

# Create your models here.
class Stock(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    token = models.CharField(max_length=300,blank=False, default='')