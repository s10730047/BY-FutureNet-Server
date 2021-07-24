from django.db import models

# Create your models here.
class Eps(models.Model):
    StockID = models.CharField(max_length=70,blank=True, null=True, default='')
    EPS2021Q1 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2020Q4 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2020Q3 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2020Q2 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2020Q1 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2019Q4 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2019Q3 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2019Q2 = models.FloatField(max_length=200,blank=True, null=True, default="0")
    EPS2019Q1 = models.FloatField(max_length=200,blank=True, null=True, default="0")