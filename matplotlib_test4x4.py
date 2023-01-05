import requests
import pandas as pd
import numpy
import json
import time
import datetime
import os.path
import matplotlib.pyplot as plt
import matplotlib

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


stockID = "1101"

fname = stockID + '_FinancialStatements_raw' +'.txt'
data = read_txt_addjsonBracket(fname)
df = pd.DataFrame(data)

#print(df)


# written by chatGPT
# Group the data by the "type" column
grouped_df = df.groupby('type')
rowlength = int(grouped_df.ngroups/4) 
# Create a figure with a subplot for each group
#fig, axs = plt.subplots(nrows=len(grouped_df), sharex=True)
fig, axs = plt.subplots(nrows=4, ncols=rowlength, sharex=True)

# Iterate through each group and plot the data in a subplot
# for i, (name, group) in enumerate(grouped_df):
#     axs[i].plot(group['date'], group['value'], label=name)
#     axs.get_yaxis().set_major_formatter( matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
#     axs[i].legend()

# Iterate through each group and plot the data in a subplot
for i, (name, group) in enumerate(grouped_df):
    axs[i // 4][i % 4].plot(group['date'], group['value'], label=name)
    axs[i // 4][i % 4].ticklabel_format(style='plain',axis='y')
    axs[i // 4][i % 4].tick_params(axis='both', which='major', labelsize=6)
    axs[i // 4][i % 4].tick_params(axis='both', which='minor', labelsize=4)
    axs[i // 4][i % 4].get_yaxis().set_major_formatter( matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    axs[i // 4][i % 4].get_xaxis().set_tick_params(rotation=30)
    axs[i // 4][i % 4].legend()


# Show the plots
plt.show()


#credit to chatGPT

# df.plot(x='date',y='value')
# df.set_index('date', inplace=True)
# df.groupby('type')['value'].plot(legend=True)
# 


# grouped = df.groupby(['type'])
# rowlength = int(grouped.ngroups/2)                         # fix up if odd number of groups
# fig, axs = plt.subplots(figsize=(9,4), 
                        # nrows=2, ncols=rowlength,     # fix as above
                        # gridspec_kw=dict(hspace=0.4)) # Much control of gridspec
# 
# targets = zip(grouped.groups.keys(), axs.flatten())
# 
# for i, (key, ax) in enumerate(targets):
    # ax.plot(x='date',y='value')
    # ax.get_yaxis().set_major_formatter( matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
# 
# ax.legend()


#fig, ax = plt.subplots()



# for key, grp in df.groupby(['type']):
    # ax.plot(grp['date'], grp['value'], label=key)
    # ax.get_yaxis().set_major_formatter( matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
# 
# ax.legend()
#plt.ticklabel_format(style='plain',axis='y')


# for stockID in Top200stock:
    # fname = stockID + '_MonthRevenue_raw' +'.txt'
    # if os.path.isfile(fname) :
        # print(stockID)
#    
#    





