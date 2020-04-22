# -*- coding: big5 -*-
import pandas as pd
import json
import numpy as np
import _mysql


def isint(n):
    try:
        int(n)
        return int(n)
    except ValueError:
        return 'null'


def isfloat(f):
    try:
        float(f)
        return float(f)
    except ValueError:
        return 'null'



def checkpara(a):
    tmp = str(a[0]).split("/")
    tmp[0] = str(int(tmp[0]) + 1911)
    a[0] = '"' + "/".join(tmp) + '"' #date
    a[1] = isint(a[1].replace(',', '')) #volume
    a[2] = isfloat(a[2].replace(',', '')) #total_amount
    a[3] = isfloat(a[3].replace(',', '')) #opening_price
    a[4] = isfloat(a[4].replace(',', '')) #high_price
    a[5] = isfloat(a[5].replace(',', '')) #low_price
    a[6] = isfloat(a[6].replace(',', '')) #closing_price
    try:
        for ch in ['+', ',']:
            a[7] = a[7].replace(ch, '')  #price_change
        for ch in ['X', 'x']:
            if ch in str(a[7]):
                a[7] = "null"
            elif a[7] == "":
                a[7] = "null"
            else:
                a[7] = float(a[7])
    except ValueError:
        print a[7]

    a[8] = isint(a[8].replace(',', '')) #transaction


def insertdata(stockname,filename):
    filepath = "/home/ubuntu/" + stockname + '/' +stockname + '_' + filename + ".json"
    #source = open("/home/ubuntu/2330/2330_201805.json" , 'r')
    source = open(filepath, 'r')
    data = source.read()
    source.close()

    db = _mysql.connect("localhost","ubuntu","ubuntu","stock")

    s = json.loads(data)
    for a in s['data'] :
        #cursor = db.cursor()
        query = "insert into daily_close_price "
        query += "(stock, date, volume, total_amount, opening_price, high_price, low_price, closing_price, price_change, transaction)"
        query += " values (" + stockname
        checkpara(a)
        for b in a :
            query += "," + str(b).decode('unicode-escape')
        query += ")"
        print query
        #cursor.execute(query)
        db.query(query)

    db.close()



