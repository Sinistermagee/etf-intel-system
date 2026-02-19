import numpy as np

def calculate_score(df):
    df = df.copy()

    # ====== 1️⃣ 均线趋势因子 ======
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()

    trend_score = 0
    if df["ma20"].iloc[-1] > df["ma60"].iloc[-1]:
        trend_score = 30
    else:
        trend_score = 10

    # ====== 2️⃣ 动量因子 ======
    momentum = (df["close"].iloc[-1] / df["close"].iloc[-20] - 1) * 100
    momentum_score = min(max(momentum, -10), 10) + 20  # 映射到10-30区间

    # ====== 3️⃣ RSI 因子 ======
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    rsi_value = rsi.iloc[-1]
    rsi_score = 20 - abs(rsi_value - 50) / 50 * 20  # 越接近50越高

    # ====== 4️⃣ 波动率惩罚 ======
    volatility = df["close"].pct_change().rolling(20).std().iloc[-1] * 100
    volatility_penalty = min(volatility, 5)

    total_score = trend_score + momentum_score + rsi_score - volatility_penalty

    return round(total_score, 2)
