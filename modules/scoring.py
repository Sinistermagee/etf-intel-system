import numpy as np

def calculate_score(df):
    close = df["close"]

    score = 0

    # ===== 1️⃣ 趋势因子 =====
    ma20 = close.rolling(20).mean().iloc[-1]
    ma60 = close.rolling(60).mean().iloc[-1]

    if ma20 > ma60:
        score += 30
    else:
        score += 10

    # ===== 2️⃣ 动量因子 =====
    momentum = (close.iloc[-1] / close.iloc[-20] - 1)

    if momentum > 0.05:
        score += 30
    elif momentum > 0:
        score += 20
    else:
        score += 5

    # ===== 3️⃣ RSI 因子 =====
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    rsi_value = rsi.iloc[-1]

    if 40 <= rsi_value <= 60:
        score += 20
    elif 30 <= rsi_value < 40 or 60 < rsi_value <= 70:
        score += 10
    else:
        score += 5

    # ===== 4️⃣ 波动率惩罚 =====
    volatility = close.pct_change().rolling(20).std().iloc[-1]

    if volatility > 0.04:
        score -= 10

    return {"total_score": round(score, 2)}
