import requests
import pandas as pd
from bs4 import BeautifulSoup 
import os
url = "https://www.taifex.com.tw/cht/3/futAndOptDate"
marginUrl = "https://histock.tw/stock/three.aspx?m=mg"
investorUrl ="https://histock.tw/stock/three.aspx"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

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
form_data = {
    'queryType': '3',
    'goDay: ': '',
    'dateaddcnt': '-1',
    'doQuery': '1',
    'queryDate' : '{Todaydate}'.format(Todaydate=date)
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
Margin = Margindf.iloc[0,1]
MarginChange = Margindf.iloc[0,2]
ShortSelling = Margindf.iloc[0,3]
ShortSellingChang = Margindf.iloc[0,4]
TAIEX = Margindf.iloc[0,5]
res4 = requests.get(investorUrl,headers=headers)
res4.encoding = "utf-8"
soup4 = BeautifulSoup(res4.text,"lxml")
data4 = soup4.find("table",class_="gvTB")
data5 = soup4.find_all("span",class_ = "clr-gr")
Fluctuation = data5[1].get_text()
Investordfs=pd.read_html(data4.prettify())
Investordf = Investordfs[0]
ForeignInvestors = Investordf.iloc[0,1]
InvestmentTrust = Investordf.iloc[0,2]
Dealer = Investordf.iloc[0,4]
abc = data5[1].get_text()
print(Fluctuation)


# print("本數據日期:",date)
# print("本日期貨多單未平倉增減:",FuturesLongVary)
# print("本日期貨空單未平倉增減:",FuturesShortVary)
# print("本日期貨淨額:" , FuturesNet)
# print("本日選擇權多單未平倉增減:",OptionLongVary)
# print("本日選擇權空單未平倉增減:",OptionShortVary)
# print("本日選擇權淨額:" , OptionNet)
os.system("pause")

############選擇權