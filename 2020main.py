
import pandas as pd
import requests
import os.path
import time

path = "G:\\code_project\\stock\\2020\\"
StockListPath = "G:\\code_project\\stock\\2020\\allstocks.csv"
url = 'http://www.tse.com.tw/exchangeReport/STOCK_DAY'
stocknum = ''



def month_year_iter( start_month, start_year, end_month, end_year ):

    for year in range(start_year,end_year+1):
        month_start =1
        month_end = 13
        if year == end_year:
            month_end = end_month+1
        if year == start_year:
            month_start = start_month
        for month in range(month_start,month_end):
            directory = path +stocknum+"\\"+stocknum+"_"+str(year)+str('{:02d}'.format(month))+".json"
            try:
                r = requests.get(url, {

                    'response': 'json',
                    'date': str(year)+str('{:02d}'.format(month))+'01',
                    'stockNo': stocknum,

                })
                #r.encoding = 'utf8'
                with open(directory, "wb") as text_file:
                    text_file.write(r.text.encode('utf-8'))
                    print (directory)
            except requests.exceptions.ConnectionError:
                r.status_code = "Connection refused"
            time.sleep(random.randint(30,40))



df = pd.read_csv(StockListPath,header=None)
data = df[[0,1]]

for index,row in data.iterrows():
    stocknum=str(row[0])
    if not os.path.exists(path + stocknum):
        os.makedirs(path + stocknum)

    startdate=(row[1])
    if startdate < 19990101:
        startdate = "19990101"
    else:
        startdate = str(startdate)
    print (stocknum+ " " + startdate)
    
    month_year_iter(int(startdate[4:6]), int(startdate[0:4]), 4, 2020)
