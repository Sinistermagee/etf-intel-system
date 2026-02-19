import akshare as ak
import pandas as pd

def get_etf_data(code):
    try:
        df = ak.fund_etf_hist_em(symbol=code)
        df = df.tail(120)
        df["close"] = df["收盘"].astype(float)
        return df
    except:
        return None
