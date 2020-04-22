import pandas as pd
import requests
import os.path
import time

url = 'http://www.tse.com.tw/exchangeReport/STOCK_DAY'
stocknum = ''


def month_year_iter2( start_month, start_year, end_month, end_year ):

    for year in range(start_year,end_year+1):
        month_start =1
        month_end = 13
        if year == end_year:
            month_end = end_month+1
        if year == start_year:
            month_start = start_month
        for month in range(month_start,month_end):
            directory = "/home/ubuntu/allstocks/" +stocknum+"/"+stocknum+"_"+str(year)+str('{:02d}'.format(month))+".json"
            try:
                r = requests.get(url, {

                    'response': 'json',
                    'date': str(year)+str('{:02d}'.format(month))+'01',
                    'stockNo': stocknum,

                })
                #r.encoding = 'utf8'
                with open(directory, "w") as text_file:
                    text_file.write(r.text.encode('utf-8'))
                    print directory
            except requests.exceptions.ConnectionError:
                r.status_code = "Connection refused"
            time.sleep(30)


df = pd.read_csv('/home/ubuntu/Desktop/all_stocks3.csv',header=None)

x = df[[1,13]]

for index,row in x.iterrows():
    stocknum=str(row[1])
    if not os.path.exists('/home/ubuntu/allstocks/' + stocknum):
        os.makedirs('/home/ubuntu/allstocks/' + stocknum)

    x=(row[13])
    if x < 19990101:
        x = "19990101"
    else:
        x = str(x)

    month_year_iter2(int(x[4:6]), int(x[0:4]), 5, 2018)
