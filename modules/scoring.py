from modules.data_fetch import get_etf_data


def calculate_score(code):

    df = get_etf_data(code)
    if df is None or len(df) < 60:
        return {
            "total_score": 0
        }

    close = df["close"]

    # ===== 10日收益 =====
    ret_10 = (close.iloc[-1] - close.iloc[-11]) / close.iloc[-11]
    score_10 = max(0, ret_10 * 800)
    score_10 = min(score_10, 40)

    # ===== 20日收益 =====
    ret_20 = (close.iloc[-1] - close.iloc[-21]) / close.iloc[-21]
    score_20 = max(0, ret_20 * 600)
    score_20 = min(score_20, 30)

    # ===== 趋势确认 =====
    ma20 = close.rolling(20).mean().iloc[-1]
    ma60 = close.rolling(60).mean().iloc[-1]

    score_trend = 30 if ma20 > ma60 else 0

    total_score = score_10 + score_20 + score_trend

    return {
        "total_score": round(total_score, 2)
    }
