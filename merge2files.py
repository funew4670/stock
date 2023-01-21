import shutil
import requests
import pandas as pd
import json
import time
import datetime
import csv

def read_txt_addjsonBracket(filename):
    with open(filename, encoding='utf-8') as data_file:
        text="["+data_file.read()
        text = text[:-2]+"]"
        data = json.loads(text)
    return data

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


#check file path first
Top200stock =json_to_df_stock_id("市值top200_20220501.json")

listTop200stock=json_to_df("市值top200_20220501.json")
#get only "公司名稱" and "stock_id" from Top200stock
Top200stockname = listTop200stock[['stock_id','公司名稱']]


#### escpae
bool_escape = False
escape_stock_id = ""
list_substract ={}


for stockID in Top200stock:

    if bool_escape :
        if stockID == escape_stock_id :
            bool_escape = False           
                
    else :
        outputName = stockID + '_raw' +'.txt'
        filepath = "C:\\" + outputName
        filepath2 = "C:\\" + outputName

        with open(filepath, 'ab') as outputfile, open(filepath2, 'rb') as file2:
            shutil.copyfileobj(file2, outputfile)
            



