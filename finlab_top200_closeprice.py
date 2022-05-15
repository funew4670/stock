from finlab import data
import time
import json
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def read_json(filename):
    with open(filename, encoding='utf-8') as data_file:
        data = json.load(data_file)
    return data


def json_to_df(filename):
    data = read_json(filename)
    df = pd.DataFrame(data)
    return df


def json_to_df_stock_id(filename):
    data = read_json(filename)
    df = pd.DataFrame(data)
    df['stock_id'] = df['stock_id'].astype(str)
    array = df['stock_id'].values
    return array



Top200stock =json_to_df_stock_id("市值top200_20220501.json")


df = data.get('price:收盤價')
df = df.loc['2022',Top200stock]

outputNameCSV = 'Top200收盤價_'+ time.strftime('%Y%m%d')+'.csv'
df.to_csv(outputNameCSV, sep='\t', encoding='utf-8')

outputX = df.to_json(orient='records',force_ascii=False)
outputName = 'Top200收盤價_'+ time.strftime('%Y%m%d')+'.json'
file = open(outputName, 'w' ,encoding='utf-8')
file.write(outputX)
file.close()
