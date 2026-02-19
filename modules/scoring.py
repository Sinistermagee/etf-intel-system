import numpy as np

def calculate_score(df):
    close = df["close"]

    ma20 = close.rolling(20).mean().iloc[-1]
    ma60 = close.rolling(60).mean().iloc[-1]
    current = close.iloc[-1]

    score = 0

    # 趋势
    if current > ma20:
        score += 20
    if ma20 > ma60:
        score += 20

    # 动量
    change_5 = (close.iloc[-1] - close.iloc[-6]) / close.iloc[-6]
    if change_5 > 0:
        score += 20

    # 简单波动控制
    volatility = np.std(close.tail(20))
    if volatility < close.mean() * 0.05:
        score += 20

    # 预留舆情因子
    score += 20

    return {"total_score": score}
