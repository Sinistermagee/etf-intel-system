import pandas as pd
import yfinance as yf

def get_etf_data(code):
    """
    返回 DataFrame, 列: 'close'
    """
    try:
        ticker = yf.Ticker(code + ".SS")  # 上证ETF代码
        hist = ticker.history(period="3mo", interval="1d")
        df = hist[["Close"]].rename(columns={"Close": "close"})
        df = df.dropna()
        return df
    except Exception as e:
        print(f"获取ETF {code} 数据失败: {e}")
        return None
