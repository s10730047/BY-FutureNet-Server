from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup 
from django.http.response import JsonResponse
import os
from rest_framework.decorators import api_view
from rest_framework import status
from Futures.models import Future
from datetime import datetime
from Futures.serializers import FutureSerializer
# Create your views here.

url = "https://www.taifex.com.tw/cht/3/futAndOptDate"
marginUrl = "https://histock.tw/stock/three.aspx?m=mg"
investorUrl ="https://histock.tw/stock/three.aspx"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

@api_view(['GET', 'POST', 'DELETE']) 

def FutureData_get(request):
    if request.method == 'GET':
        res = requests.post(url,headers = headers)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text,"lxml")
        data = soup.find("table",{'width':'100%'})
        date = soup.find('input',{'id' :'queryDate'}).get('value') #取得期交所表單日期
        dfs = pd.read_html(data.prettify())
        df = dfs[0]
        TodayFuturesLongOpenPosition = df.iloc[17,1] #本日期貨多單未平倉
        TodayFuturesShortOpenPosition =df.iloc[17,5] #本日期貨空單未平倉
        TodayOptionLongOpenPosition = df.iloc[17,2] #本日選擇權多單未平倉
        TodayOptionShortOpenPosition = df.iloc[17,6] #本日選擇權空單未平倉
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
        res2 = requests.post(url,headers = headers, data=form_data)
        res2.encoding = "utf-8"
        soup2 = BeautifulSoup(res2.text,"lxml")
        data2 = soup2.find("table",{'width':'100%'})
        LastDaydfs = pd.read_html(data2.prettify())
        LastDaydf = LastDaydfs[0]
        LastDayFuturesLongOpenPosition = LastDaydf.iloc[17,1] #昨日期貨多單未平倉
        LastDayFuturesShortOpenPosition =LastDaydf.iloc[17,5] #昨日期貨空單未平倉
        LastDayOptionLongOpenPosition = df.iloc[17,2] #昨日選擇權多單未平倉
        LastDayOptionShortOpenPosition = df.iloc[17,6] #昨日選擇權空單未平倉
        FuturesNet =int(LastDayFuturesLongOpenPosition)-int(LastDayFuturesShortOpenPosition) #期貨淨額
        OptionNet =int(LastDayOptionLongOpenPosition)-int(LastDayOptionShortOpenPosition) #選擇權淨額
        FuturesLongVary =int(TodayFuturesLongOpenPosition)-int(LastDayFuturesLongOpenPosition) #本日期貨多單未平倉增減
        FuturesShortVary = int(TodayFuturesShortOpenPosition)-int(LastDayFuturesShortOpenPosition) #本日期貨空單未平倉增減
        OptionLongVary = int(TodayFuturesLongOpenPosition)-int(LastDayOptionLongOpenPosition) #本日選擇權多單未平倉增減
        OptionShortVary = int(TodayFuturesShortOpenPosition)-int(LastDayOptionShortOpenPosition) #本日選擇權空單未平倉增減
        res3 = requests.get(marginUrl,headers = headers)
        res3.encoding = "utf-8"
        soup3 = BeautifulSoup(res3.text,"lxml")
        data3 = soup3.find("table",class_="gvTB")
        Margindfs = pd.read_html(data3.prettify())
        Margindf = Margindfs[0]
        Margin = Margindf.iloc[0,1] #融資
        MarginChange = Margindf.iloc[0,2] # 融資增減
        ShortSelling = Margindf.iloc[0,3] #融券
        ShortSellingChang = Margindf.iloc[0,4] #融券增減
        TAIEX = Margindf.iloc[0,5] #加權指數
        res4 = requests.get(investorUrl,headers=headers)
        res4.encoding = "utf-8"
        soup4 = BeautifulSoup(res4.text,"lxml")
        data4 = soup4.find("table",class_="gvTB")
        data5 = soup4.find_all("span",class_ = "clr-gr") 
        Fluctuation = data5[1].get_text()
        Investordfs=pd.read_html(data4.prettify())
        Investordf = Investordfs[0]
        ForeignInvestors = Investordf.iloc[0,1] #外資
        InvestmentTrust = Investordf.iloc[0,2] #投信
        Dealer = Investordf.iloc[0,4] #自營商 
        Future.objects.create(
            Date = date,
            TAIEX = TAIEX,
            Fluctuation = Fluctuation,
            ForeignInvestors = ForeignInvestors,
            InvestmentTrust = InvestmentTrust,
            Dealer = Dealer,
            Margin = Margin,
            MarginChange = MarginChange,
            ShortSelling = ShortSelling,
            ShortSellingChang = ShortSellingChang,
            FuturesLongOpenPosition = TodayOptionLongOpenPosition,
            FuturesShortOpenPosition = TodayOptionShortOpenPosition,
            FuturesNet = FuturesNet,
            FuturesLongVary = FuturesLongVary,
            FuturesShortVary = FuturesShortVary
            )
        content = {'msg': '資料取得成功'}
        return JsonResponse(content, status=status.HTTP_201_CREATED)

def GetFutureData(request):
    if request.method == 'GET':
        data =Future.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            data = data.filter(title_icontains=title)
        futures_serializer = FutureSerializer(data,many=True)
        return JsonResponse(futures_serializer.data, safe=False)