from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
from eps.models import Eps
from eps.serializers import EpsSerializer
from rest_framework.decorators import api_view
import pandas as pd
from bs4 import BeautifulSoup 
import requests
import twstock
url = "https://histock.tw/stock/"
name ='/每股盈餘'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

@api_view(['GET', 'POST', 'DELETE']) 

def eps_get(request):
     if request.method == 'POST':
        stockID = request.data.get("StockID",0)
        res = requests.get(url+stockID+name,headers = headers)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text,"lxml")
        data = soup.find("table",class_="tb-stock text-center tbBasic")
        dfs = pd.read_html(data.prettify())
        df = dfs[0]
        Eps2021Q1 =df.iloc[0,9]
        Eps2020Q4 =df.iloc[0,8]
        Eps2020Q3 =df.iloc[1,8]
        Eps2020Q2 =df.iloc[2,8]
        Eps2020Q1 =df.iloc[3,8]
        Eps2019Q4 =df.iloc[0,7]
        Eps2019Q3 =df.iloc[1,7]
        Eps2019Q2 =df.iloc[2,7]
        Eps2019Q1 =df.iloc[3,7]
        PERres = requests.get(url+stockID,headers=headers)
        PERres.encoding = "utf-8"
        soup2 = BeautifulSoup(PERres.text,"lxml")
        data2 = soup2.find("table",class_="tb-stock tbBasic")
        priceDfs =pd.read_html(data2.prettify())
        priceDf =priceDfs[0]
        Per = priceDf.iloc[2,1]
        TrueEpsGrowPercent = round((float(Eps2021Q1)-float(Eps2020Q1))/float(Eps2020Q1),4)#已確定2021比2020Q1 成長%數
        LastQ1EpsGrowPercent = round((float(Eps2020Q1)-float(Eps2019Q1))/float(Eps2019Q1),4) #2019-2020 Q1成長%數
        LastQ2EpsGrowPercent = round((float(Eps2020Q2)-float(Eps2019Q2))/float(Eps2019Q2),4) #2019-2020 Q2成長%數
        LastQ3EpsGrowPercent = round((float(Eps2020Q3)-float(Eps2019Q3))/float(Eps2019Q3),4) #2019-2020 Q3成長%數
        LastQ4EpsGrowPercent = round((float(Eps2020Q4)-float(Eps2019Q4))/float(Eps2019Q4),4) #2019-2020 Q4成長%數
        TotalEpsGrowPercent = (TrueEpsGrowPercent-LastQ1EpsGrowPercent)/LastQ1EpsGrowPercent #TEGP比LEGP多成長
        Estimate2021Q2Grow = round(LastQ2EpsGrowPercent*TotalEpsGrowPercent+LastQ2EpsGrowPercent,4) #預估 2021比2020 Q2成長%數
        Estimate2021Q3Grow = round(LastQ3EpsGrowPercent*TotalEpsGrowPercent+LastQ3EpsGrowPercent,4) #預估 2021比2020 Q3成長%數
        Estimate2021Q4Grow = round(LastQ4EpsGrowPercent*TotalEpsGrowPercent+LastQ4EpsGrowPercent,4) #預估 2021比2020 Q4成長%數
        Estimate2021Q1Eps = round(float(Eps2020Q1)*(1+TrueEpsGrowPercent),4) #預估2021 Q1 EPS
        Estimate2021Q2Eps = round(float(Eps2020Q2)*(1+Estimate2021Q2Grow),4) #預估2021 Q2 EPS
        Estimate2021Q3Eps = round(float(Eps2020Q3)*(1+Estimate2021Q3Grow),4) #預估2021 Q3 EPS
        Estimate2021Q4Eps = round(float(Eps2020Q4)*(1+Estimate2021Q4Grow),4) #預估2021 Q4 EPS 
        Estimate2021Eps = Estimate2021Q1Eps+Estimate2021Q2Eps+Estimate2021Q3Eps+Estimate2021Q4Eps
        EstimateReasonablePrice =Estimate2021Eps*float(Per)
        Eps.objects.create(
            StockID = stockID,
            EPS2021Q1=Eps2021Q1,
            EPS2020Q4=Eps2020Q4,
            EPS2020Q3=Eps2020Q3,
            EPS2020Q2=Eps2020Q2,
            EPS2020Q1=Eps2020Q1,
            EPS2019Q4=Eps2019Q4,
            EPS2019Q3=Eps2019Q3,
            EPS2019Q2=Eps2019Q2,
            EPS2019Q1=Eps2019Q1
            )
        content = {'msg': 'Eps取得成功'}
        return JsonResponse(content, status=status.HTTP_201_CREATED)
    # content = {'msg': '代號輸入錯誤或是此代號為ETF'} 
    # return JsonResponse(content,eps_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

