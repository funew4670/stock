import requests
import os.path
import time
stocknum = '2330'
url = 'http://www.tse.com.tw/exchangeReport/STOCK_DAY'

if not os.path.exists('/home/ubuntu/' + stocknum):
    os.makedirs('/home/ubuntu/' + stocknum)


def month_year_iter2( start_month, start_year, end_month, end_year ):

    for year in range(start_year,end_year+1):
        month_start =1
        month_end = 13
        if year == end_year:
            month_end = end_month+1
        if year == start_year:
            month_start = start_month
        for month in range(month_start,month_end):
            time.sleep(6)
            directory = "/home/ubuntu/" +stocknum+"/"+stocknum+"_"+str(year)+str('{:02d}'.format(month))+".json"
            r = requests.get(url, {

                'response': 'json',
                'date': str(year)+str('{:02d}'.format(month))+'01',
                'stockNo': stocknum,

            })
            #r.encoding = 'utf8'
            with open(directory, "w") as text_file:
                text_file.write(r.text)


month_year_iter2(2,2000,5,2000)
