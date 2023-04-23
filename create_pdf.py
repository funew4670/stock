#create pdf

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph ,Image
import requests
import pandas as pd
import numpy
import json
import time
import datetime
import os.path
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
import matplotlib.dates as mdates


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
    df_id_name_capital = df[["stock_id","公司簡稱","實收資本額(元)"]]
    df_id_name_capital['stock_id'] = df_id_name_capital['stock_id'].astype(str)    
    return df

Top200stock =json_to_df_stock_id("市值top200_20220501.json")

# Sort the dataframe by "price" column in ascending order
Top200stock_sorted = Top200stock.sort_values(by="實收資本額(元)",ascending=False )

# 拿預設樣式
styles = getSampleStyleSheet()

styleNormalCustom = ParagraphStyle(
    'styleNormalCustom',
    fontName='kaiu',
    parent=styles["Normal"],
    fontSize=20,
    alignment=TA_CENTER,
    textColor=colors.black,
    spaceBefore = 20,
    spaceAfter =20

)

styleNormalCustom_sub = ParagraphStyle(
    'styleNormalCustom',
    fontName='kaiu',
    parent=styles["Normal"],
    fontSize=12,
    alignment=TA_LEFT ,
    textColor=colors.black,
    spaceBefore = 12,
    spaceAfter =12

)





pdfmetrics.registerFont(TTFont('kaiu', "font/kaiu.ttf"))

fileName = "example.pdf"
pdfTemplate = SimpleDocTemplate(fileName)
story = []


for index, row in Top200stock_sorted.iterrows():
    print (row["stock_id"])
    print (row["公司簡稱"])
    print (row["實收資本額(元)"])
    story.append(Paragraph(row["公司簡稱"]+str(row["stock_id"]), styleNormalCustom))
    story.append(Paragraph("資本額:"+'{:,}'.format(row["實收資本額(元)"]), styleNormalCustom_sub))
    imagepath = "pic\\MonthRevenue\\"+str(row["stock_id"]) + '_revenue' +'.png'
    image = Image(imagepath, width=400, height=200)
    story.append(image)

pdfTemplate.build(story)
