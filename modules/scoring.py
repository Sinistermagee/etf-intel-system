from modules.data_fetch import get_etf_data


def calculate_score(code):

    df = get_etf_data(code)
    if df is None or len(df) < 60:
        return 0

    close = df["close"]

    score = 0

    # ===== 1️⃣ 10日动量（40分）=====
    ret_10 = (close.iloc[-1] - close.iloc[-11]) / close.iloc[-11]
    if ret_10 > 0:
        score += 40

    # ===== 2️⃣ 20日动量（30分）=====
    ret_20 = (close.iloc[-1] - close.iloc[-21]) / close.iloc[-21]
    if ret_20 > 0:
        score += 30

    # ===== 3️⃣ 趋势确认（30分）=====
    ma20 = close.rolling(20).mean().iloc[-1]
    ma60 = close.rolling(60).mean().iloc[-1]

    if ma20 > ma60:
        score += 30

    return score
