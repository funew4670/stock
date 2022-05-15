#load Top200收盤價_20220501.json into pandas and caculate moving average at window size of 20

import json
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os.path

def read_json(filename):
    with open(filename, encoding='utf-8') as data_file:
        data = json.load(data_file)
    return data


def json_to_df(filename):
    data = read_json(filename)
    df = pd.DataFrame(data)
    return df

filename =  'Top200收盤價_'+ time.strftime('%Y%m%d')+'.json'

#check if the file exists
if not os.path.isfile(filename):
    print('file not found')
    exit()

df = json_to_df(filename)
ma = df.rolling(window=20).mean()
std = df.rolling(window=20).std()

#print(df['2330'])
##print(ma['2330'])
#print(std['2330'])

#using numpy to caculate Bollinger upper Band and lower Band
upperBand = ma + 2*std
lowerBand = ma - 2*std

#subtract lowerBand from df and divide by 100 to get percentage
substract = (df - lowerBand)/100


#get substract last row
lastrow = substract.iloc[-1]

#print last row order by value
#print(lastrow.sort_values(ascending=False))

#load 市值top200_20220501.json and get 
Top200stock =json_to_df("市值top200_20220501.json")

#get only "公司名稱" and "stock_id" from Top200stock
Top200stockname = Top200stock[['stock_id','公司名稱']]

#join lastrow and Top200stockname by lastrow.index and Top200stockname.stock_id 
result = pd.merge(lastrow,Top200stockname,left_index=True,right_on='stock_id')

#get the first column name
columns = result.columns.values

#rename result first column name 74 to "substractPercent"
result.rename(columns={columns[0]:'substractPercent'},inplace=True)


#print result order by substractPercent ASC
print(result.sort_values(by='substractPercent',ascending=True))

#output result to csv
outputNameCSV = 'Top200收盤價布林通道下限差_'+ time.strftime('%Y%m%d')+'.csv'
result.to_csv(outputNameCSV, sep=',', encoding='utf-8')

#output result to pdf
#outputNamePDF = 'Top200收盤價布林通道下限差_'+ time.strftime('%Y%m%d')+'.pdf'
#result.to_pdf(outputNamePDF, encoding='utf-8')




plt.plot(df['8454'])
plt.plot(ma['8454'])
plt.plot(std['8454'])
plt.plot(upperBand['8454'])
plt.plot(lowerBand['8454'])
plt.show()

print()


