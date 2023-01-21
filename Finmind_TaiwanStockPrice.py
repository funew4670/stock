import requests
import pandas as pd
import time
import json
import datetime

url = "https://api.finmindtrade.com/api/v4/data"

data_id = ""
token = ""


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


parameter = {
    "dataset": "TaiwanStockPrice",
    "data_id": data_id,
    "start_date": "2020-01-01",
    "end_date": "2022-12-9",
    "token": token, # 參考登入，獲取金鑰
}


Top200stock =json_to_df_stock_id("市值top200_20220501.json")

for sotckID in Top200stock:
    print("getting data stock_id =" + sotckID)

    parameter["data_id"] = sotckID
    resp = requests.get(url, params=parameter)
    data = resp.json()
    data = pd.DataFrame(data["data"])
    print(data.head())
   
    outputName = sotckID + '_raw' +'.txt'
    outputX = data.to_json(orient='records',force_ascii=False)
    outputX = outputX.strip("[]")
    outputX = outputX.replace("},","},\n")
    outputX = outputX + ",\n"
    file = open(outputName, 'w' ,encoding='utf-8')
    #for line in outputX:
    #        #file.write(f"{line}\n")
    file.write(outputX)
    file.close()

    print(datetime.datetime.now())
    time.sleep(60)
    #使用次數

    url_usr = "https://api.web.finmindtrade.com/v2/user_info"
    payload = {
        "token": token,
    }
    resp_usr = requests.get(url_usr, params=payload)
    usercount = resp_usr.json()["user_count"]  # 使用次數
    request = resp_usr.json()["api_request_limit"]  # api 使用上限
    print("usercount:"+str(usercount)+"/"+str(request))
    if usercount > 580 :
        exit()

    time.sleep(10)

