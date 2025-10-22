import pandas as pd
import requests
from io import StringIO

def get_sp500():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    html = StringIO(response.text)  # ✅ wrap the HTML string
    
    df = pd.read_html(html)[0]  # now no warning
    
    cols = ["Symbol", "Security", "GICS Sector", "GICS Sub-Industry"]
    df = df[cols].rename(columns={
        "Symbol": "symbol",
        "Security": "name",
        "GICS Sector": "sector",
        "GICS Sub-Industry": "subIndustry",
    })
    
    return df



sp500 = get_sp500()
sp500.to_csv("sp500_companies.csv", index=False)
