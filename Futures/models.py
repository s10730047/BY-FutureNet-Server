from django.db import models

# Create your models here.
class Future(models.Model):
    Date = models.CharField(max_length=50,blank=True,null=True, default='') #日期
    TAIEX = models.CharField(max_length=50,blank=True, null=True, default="0") #加權指數
    Fluctuation = models.CharField(max_length=50,blank=True, null=True, default="0") #漲跌
    ForeignInvestors = models.CharField(max_length=50,blank=True, null=True, default="0") #外資
    InvestmentTrust = models.CharField(max_length=50,blank=True, null=True, default="0") #投信
    Dealer = models.CharField(max_length=50,blank=True, null=True, default="0") #自營商
    Margin = models.CharField(max_length=50,blank=True, null=True, default="0") #融資
    MarginChange = models.CharField(max_length=50,blank=True, null=True, default="0") #融資增減
    ShortSelling = models.CharField(max_length=50,blank=True, null=True, default="0") #融券
    ShortSellingChang = models.CharField(max_length=50,blank=True, null=True, default="0") #融券增減
    FuturesLongOpenPosition = models.CharField(max_length=50,blank=True, null=True, default="0") #期貨未平倉多單
    FuturesShortOpenPosition = models.CharField(max_length=50,blank=True, null=True, default="0") #期貨未平倉空單
    FuturesNet = models.CharField(max_length=50,blank=True, null=True, default="0") #期貨淨額
    FuturesLongVary = models.CharField(max_length=50,blank=True, null=True, default="0") #期貨多單增減
    FuturesShortVary = models.CharField(max_length=50,blank=True, null=True, default="0") #期貨空單增減
    def __str__(self):
        return self.body