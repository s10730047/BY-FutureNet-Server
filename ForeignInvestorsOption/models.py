from django.db import models

# Create your models here.
class ForeignInvestorsOption(models.Model):
    Date = models.CharField(max_length=50,blank=True,null=True, default='') #日期
    FuturesClosingPrice = models.IntegerField(max_length=50,blank=True, null=True, default="0") #期貨收盤價
    Fluctuation = models.CharField(max_length=50,blank=True, null=True, default="0") #漲跌
    BuyCall = models.IntegerField(max_length=50,blank=True, null=True, default="0") #買買權
    BuyCallChange = models.IntegerField(max_length=50,blank=True, null=True, default="0") #買買權變化
    BuyPut = models.IntegerField(max_length=50,blank=True, null=True, default="0") #買賣權
    BuyPutChange = models.IntegerField(max_length=50,blank=True, null=True, default="0") #買賣權變化
    SellCall = models.IntegerField(max_length=50,blank=True, null=True, default="0") #賣買權
    SellCallChange = models.IntegerField(max_length=50,blank=True, null=True, default="0") #賣買權變化
    SellPut = models.IntegerField(max_length=50,blank=True, null=True, default="0") #賣賣權
    SellPutChange = models.IntegerField(max_length=50,blank=True, null=True, default="0") #賣賣權變化
    BuyNet = models.IntegerField(max_length=50,blank=True, null=True, default="0") #買方淨額
    SellNet = models.IntegerField(max_length=50,blank=True, null=True, default="0") #賣方淨額
    BuyOpenPosition = models.FloatField(max_length=50,blank=True, null=True, default="0") #買權未平倉
    SellOpenPosition = models.FloatField(max_length=50,blank=True, null=True, default="0") #賣權未平倉