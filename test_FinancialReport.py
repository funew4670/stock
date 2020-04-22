import requests
import pandas as pd

url = 'http://mops.twse.com.tw/mops/web/ajax_t163sb04'
r = requests.post(url, {
    'encodeURIComponent': 1,
    'step': 1,
    'firstin': 1,
    'off': 1,
    'TYPEK': 'sii',
    'year': '106',
    'season': '01',
})

r.encoding = 'utf8'
dfs = pd.read_html(r.text)
print dfs

