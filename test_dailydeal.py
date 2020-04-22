台灣證券交易所 個股日成交
http://www.tse.com.tw/exchangeReport/STOCK_DAY?
response=json&date=20180522&stockNo=2330&_=1526963258755



import requests
import pandas as pd

url = 'http://www.tse.com.tw/exchangeReport/STOCK_DAY'
r = requests.get(url, {

    'response': 'json',
    'date': '20180401',
    'stockNo': '2330',

})

r.encoding = 'utf8'

print r.text
