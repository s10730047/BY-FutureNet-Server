import twstock
import matplotlib.pyplot as plt
import pandas as pd

stock_6207 = twstock.Stock('6207')
stock_6207_2018 = stock_6207.fetch_from(2018,1)     # 獲取 2018 年 01 月至今日之股票資料
stock_6207_2018_pd = pd.DataFrame(stock_6207_2018)
stock_6207_2018_pd = stock_6207_2018_pd.set_index('date')
twstock.realtime.get('2330')
print(twstock.codes['2330'])

# fig = plt.figure(figsize=(10, 6))
# plt.plot(stock_6207_2018_pd.close, '-' , label="收盤價")
# plt.plot(stock_6207_2018_pd.open, '-' , label="開盤價")
# plt.title('雷科股份2018 開盤/收盤價曲線',loc='right')
# # loc->title的位置
# plt.xlabel('日期')
# plt.ylabel('收盤價')
# plt.grid(True, axis='y')
# plt.legend()
# fig.savefig('day20_01.png')
