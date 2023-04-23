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
    df['stock_id'] = df['stock_id'].astype(str)
    array = df['stock_id'].values
    return array

Top200stock =json_to_df_stock_id("市值top200_20220501.json")

#stockID = "1101"
count = 0


for stockID in Top200stock:
    # test mode 
    # only 2330
    #if stockID != "2330"  :
    #    break
    #count += 1
    #if count < 156 :
    #    continue
    #print (count)    
    #print (stockID)    

    fname = "MonthRevenue\\"+stockID + '_MonthRevenue_raw' +'.txt'
    data = read_txt_addjsonBracket(fname)
    df = pd.DataFrame(data)
    #print(df)

    
    # # Extract date and revenue values from JSON data
    dates = [datetime.datetime.strptime(d["date"], "%Y-%m-%d") for d in data]
    revenues = [d["revenue"] for d in data]

    # written by chatGPT
    # Group the data by the "type" column
    #grouped_df = df.groupby('type')
    #rowlength = int(grouped_df.ngroups/4) 

    sum_of_values = sum( revenues)
    length_of_group = len(revenues)
    average = sum_of_values / length_of_group
    #count scientific notation divisor (string) turn to int
    power = int(math.log10(average))
    #ound a value to the nearest multiple of 3
    rounded_power = (power // 3) * 3        
    #get the y axis interval modify in the power 3,6,9...
    divisor_sci = float("{:.0e}".format(math.pow(10, rounded_power)))

    #divide with divisor_sci
    revenues_copy = revenues.copy()
    revenues_copy = [revenue / divisor_sci for revenue in revenues_copy]

    
    print(divisor_sci)
    
    # Create a plot
    fig, ax = plt.subplots(figsize=(12, 7))


    # # Create a line chart
    #plt.plot(dates, revenues_copy)
    ax.plot(dates, revenues_copy )

    # Convert the date values to datetime objects
    #dates = [mdates.datestr2num(date) for date in dates]

        

    #index_locator = ticker.IndexLocator(base=1, offset=0)
    #ax.xaxis.set_major_locator(index_locator)


    # # Set labels and title
    yLabel = ""
    unit =""
    # Add labels and title
    if rounded_power == 3:
        yLabel = "Revenue (in 1000 of NT$)"
        unit = "M"
    elif rounded_power == 6:
        yLabel = "Revenue (in millions of NT$)"
        unit = "MM"
    elif rounded_power == 9:
        yLabel = "Revenue (in billions of NT$)"
        unit = "B"
    title = "stock " +stockID+ " Revenue"

    ax.set_xlabel("dates")
    #ax.tick_params(axis='x', labelsize=6)
    ax.tick_params(axis='x', rotation=30)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    #ax.legend(loc="upper left")    
    ax.ticklabel_format(style='plain', axis='y')
    
    # Set custom tick locations and labels on the x-axis     
    #index_locator = ticker.IndexLocator(base=30, offset=0.5)
    #ax.xaxis.set_major_locator(index_locator)  # Set the major locator to DateLocator
    #ax.xaxis.set_major_locator(mdates.DateLocator())  # Set the major locator to DateLocator
    #ax.xaxis.set_minor_locator(ticker.IndexLocator(base=1, offset=0))  # Set the minor locator to IndexLocator

    ax.grid(True, linestyle='--')
  

    # Add annotations for maximum and minimum values
    max_value = max(revenues)
    min_value = min(revenues)
    max_index = revenues.index(max_value)
    min_index = revenues.index(min_value)
    y_annotation_offset = -0.2
    ax.annotate(("Max: {:.2f}"+unit).format(max_value/divisor_sci), xy=(dates[max_index], max_value//divisor_sci+y_annotation_offset) )
    ax.annotate(("Min: {:.2f}"+unit).format(min_value/divisor_sci), xy=(dates[min_index], min_value//divisor_sci+y_annotation_offset) )

    


    # # Show the chart
    #plt.show()
    
    # Save the chart to a file
    outputname ="pic\\MonthRevenue\\"+stockID + '_revenue' +'.png'
    #plt.savefig("outputname.png")
    plt.savefig(outputname)
    plt.close()
    




