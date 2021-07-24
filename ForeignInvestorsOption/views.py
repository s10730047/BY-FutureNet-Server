from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup 
import os
from datetime import datetime
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from ForeignInvestorsOption.models import ForeignInvestorsOption
from ForeignInvestorsOption.serializers import ForeignInvestorOptionSerializer
# Create your views here.
url = "https://www.taifex.com.tw/cht/3/futDailyMarketReport"
url2 = "https://www.taifex.com.tw/cht/3/callsAndPutsDate"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

@api_view(['GET', 'POST', 'DELETE']) 

def ForeignInvestorsOption_get(request):
    if request.method == 'GET':
        res2 = requests.post(url2,headers = headers)
        res2.encoding = "utf-8"
        soup2 = BeautifulSoup(res2.text,"lxml")
        data2 = soup2.find("table",class_="table_f")
        date = soup2.find('input',{'id' :'queryDate'}).get('value') #取得期交所表單日期
        dfs2 = pd.read_html(data2.prettify())
        df2 = dfs2[0]
        TodayWeekDay =datetime.today().weekday()
        if(TodayWeekDay == 1):
            dateaddcnt = -3
        else:
            dateaddcnt = -1
        form_data = {
            'queryType': '3',
            'goDay: ': '',
            'doQuery': '1',
            'dateaddcnt': '{dateaddcnt}'.format(dateaddcnt = dateaddcnt),
            'queryDate' : '{Todaydate}'.format(Todaydate=date),
            'commodityId':''
        }
        res3 = requests.post(url2,headers = headers, data=form_data)
        res3.encoding = "utf-8"
        soup3 = BeautifulSoup(res3.text,"lxml")
        data3 = soup3.find("table",class_="table_f")
        LastDaydfs = pd.read_html(data3.prettify())
        LastDaydf = LastDaydfs[0]
        form_data2 = {
            'queryType': '2',
            'marketCode': '0',
            'dateaddcnt': '{dateaddcnt}'.format(dateaddcnt = dateaddcnt),
            'commodity_id': 'TX',
            'commodity_id2': '',
            'queryDate': '{Todaydate}'.format(Todaydate=date),
            'MarketCode': '0',
            'commodity_idt': 'TX',
            'commodity_id2t': '',
            'commodity_id2t2': ''
        }

        res = requests.post(url,headers = headers,data=form_data2)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text,"lxml")
        data = soup.find("table",class_="table_f")
        dfs = pd.read_html(data.prettify())
        df = dfs[0]
        FuturesClosingPrice = df.iloc[0,5]
        Fluctuation = df.iloc[0,6]
        TodayBuyCall = df2.iloc[5,10]
        TodayBuyPut = df2.iloc[5,12]
        TodaySellCall = df2.iloc[8,10]
        TodaySellPut = df2.iloc[8,12]
        YesterdayBuyCall = LastDaydf.iloc[5,10]
        YesterdayBuyPut = LastDaydf.iloc[5,12]
        YesterdaySellCall = LastDaydf.iloc[8,10]
        YesterdaySellPut = LastDaydf.iloc[8,12]
        BuyCallChange = int(TodayBuyCall)-int(YesterdayBuyCall)
        BuyPutChange = int(TodayBuyPut)-int(YesterdayBuyPut)
        SellCallChange = int(TodaySellCall)-int(YesterdaySellCall)
        SellPutChange = int(TodaySellPut)-int(YesterdaySellPut)
        BuyNet = int(TodayBuyCall)-int(TodayBuyPut)
        SellNet = int(TodaySellCall)-int(TodaySellPut)
        TodayBuyOpenPosition = df2.iloc[5,15]
        TodaySellOpenPosition = df2.iloc[8,15]
        BuyOpenPosition = round((int(TodayBuyOpenPosition)/100000),2)
        SellOpenPosition = round((int(TodaySellOpenPosition)/100000),2)
        ForeignInvestorsOption.objects.create(
            Date = date,
            FuturesClosingPrice = FuturesClosingPrice,
            Fluctuation = Fluctuation,
            BuyCall = TodayBuyCall,
            BuyCallChange = BuyCallChange,
            BuyPut = TodayBuyPut,
            BuyPutChange = BuyPutChange,
            SellCall = TodaySellCall,
            SellCallChange = SellCallChange,
            SellPut = TodaySellPut,
            SellPutChange = SellPutChange,
            BuyNet = BuyNet,
            SellNet = SellNet,
            BuyOpenPosition = BuyOpenPosition,
            SellOpenPosition = SellOpenPosition
        )
    content = {'msg': '資料取得成功'}
    return JsonResponse(content, status=status.HTTP_201_CREATED)

def GetForeignOptionData(request):
    if request.method == 'GET':
        data = ForeignInvestorsOption.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            data = filter(title_icontains=title)
        ForeignInvestorsOption_serializer = ForeignInvestorOptionSerializer(data,many=True)
        return JsonResponse(ForeignInvestorsOption_serializer.data, safe=False)
