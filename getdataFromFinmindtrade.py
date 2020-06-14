import json
import requests
import pandas as pd
import json

data = None

with open('TaiwanStockInfo.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    data = data['data']

total_stock_count=0 
keys = list(data)

def GetFilebyStockNumber( start_id ):
    url = "http://api.finmindtrade.com/api/v2/data"
    parameter = {
        "dataset": "TaiwanStockPrice",
        "stock_id":start_id,
        "date": "1995-01-01",
        "end_date": "2020-05-29",
    }
    resp = requests.get(url, params=parameter)
    data = resp.json()
    #data = pd.DataFrame(data["data"])
    #print(data.head())
    filename =start_id+'.json' 
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#check how many stocks
if (data ==None):
    quit()
for x in keys:
    count = len(data[x])
    if (count != total_stock_count):
        if(total_stock_count == 0):
           total_stock_count= count
        else:
            print("number of stocks not match in data array keys "+x)
    print(x)
print(total_stock_count)

liststock=list()

for i in range(total_stock_count):
    row = {}
    for rowkey in keys:
        row[rowkey] = data[rowkey][i]
    liststock.append(row)

#print (len(liststock))

for row in liststock:
    GetFilebyStockNumber(row("stock_id"))
    







 




    


   



