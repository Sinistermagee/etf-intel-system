from modules.data_fetch import get_etf_data
import numpy as np


def get_market_sentiment():

    df = get_etf_data("510300")
    if df is None:
        return "市场情绪：数据异常"

    close = df["close"]

    current = close.iloc[-1]
    ma20 = close.rolling(20).mean().iloc[-1]

    # ===== 条件1：趋势 =====
    trend_ok = current > ma20

    # ===== 条件2：短期跌幅 =====
    change_3 = (close.iloc[-1] - close.iloc[-4]) / close.iloc[-4]
    drawdown_ok = change_3 > -0.03

    # ===== 条件3：波动率 =====
    volatility = close.pct_change().rolling(20).std().iloc[-1]
    volatility_ok = volatility < 0.03

    if trend_ok and drawdown_ok and volatility_ok:
        return "市场情绪：Risk On（允许进攻）"
    else:
        return "市场情绪：Risk Off（控制仓位）"
