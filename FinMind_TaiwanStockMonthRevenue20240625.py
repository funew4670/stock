import requests
import pandas as pd
import json
import time
import datetime
from dateutil.relativedelta import relativedelta
import os


url = "https://api.finmindtrade.com/api/v4/data"
token = ""
data_id = ""
parameter = {
    "dataset": "TaiwanStockMonthRevenue",
    "data_id": data_id,
    "start_date": "",
    "end_date": "",
    "token": token, # 參考登入，獲取金鑰
    #"start_date": "2020-12-01", "end_date": "2022-12-9",
}

datapath = r""
today_date = datetime.datetime.now().strftime('%Y-%m-%d')

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


def check_token_limit():
    url_usr = "https://api.web.finmindtrade.com/v2/user_info"
    payload = {
       "token": token,
    }
    resp_usr = requests.get(url_usr, params=payload)
    usercount = resp_usr.json()["user_count"]  # 使用次數
    request = resp_usr.json()["api_request_limit"]  # api 使用上限
    print("usercount "+str(usercount)+"/"+str(request))
    if usercount > 580 :
       exit()
    time.sleep(10)
    return True

def getStartDate(stockID,dataset):

    filename = stockID+"_"+ dataset + "_raw.txt"
    filepath = os.path.join(datapath,filename)

    # Read the last line of the text file
    with open(filepath, 'r',encoding='utf-8') as file:
        last_line = file.readlines()[-1]
    # Extract the date from the last line
    date_str = last_line.split('"date":"')[1].split('"')[0]

    # Convert the date string to a datetime object
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    # Add three months to the date
    #new_date = date + timedelta(days=2*30)
    # Format the new date back to the string format
    #new_date_str = new_date.strftime("%Y-%m-%d")

    # Add one month to the current date
    new_date = date + relativedelta(months=1)
    new_date_str = new_date.strftime("%Y-%m-%d")

    return new_date_str



def output_data(sotckID):
   print("getting data stock_id =" + sotckID)
   parameter["data_id"] = sotckID
   parameter["start_date"] = getStartDate(stockID,"MonthRevenue")
   parameter['end_date'] = today_date
   resp = requests.get(url, params=parameter)
   data = resp.json()
   data = pd.DataFrame(data["data"])
   print(data.head())
   outputName = "temp\\"+sotckID + '_MonthRevenue_raw' +'.txt'
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
   time.sleep(30)
   


with open('FinMind_setting.json', 'r') as file:
    setting_json = json.load(file)


parameter['start_date'] = setting_json['last_enddate'] 
parameter['end_date'] = today_date
parameter['token'] = setting_json['token'] 


Top200stock =json_to_df_stock_id("市值top200_20220501.json")




#### escpae
bool_escape = False
escape_stock_id = ""

for stockID in Top200stock:

    if bool_escape :
        if stockID == escape_stock_id :
            output_data(stockID)
            bool_escape = False           
                
    else :
        output_data(stockID)
        

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 

 
 
 
 
 
 
 
 
 
 
 














