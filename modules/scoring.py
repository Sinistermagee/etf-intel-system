def calculate_score(df):
    """
    输入: 单个ETF的历史数据df
    输出: dict，包含 total_score
    """

    if df is None or len(df) < 60:
        return {"total_score": 0}

    close = df["close"]

    # ===== 1️⃣ 10日动量 =====
    ret_10 = (close.iloc[-1] - close.iloc[-11]) / close.iloc[-11]
    score_10 = max(0, ret_10 * 800)
    score_10 = min(score_10, 40)

    # ===== 2️⃣ 20日动量 =====
    ret_20 = (close.iloc[-1] - close.iloc[-21]) / close.iloc[-21]
    score_20 = max(0, ret_20 * 600)
    score_20 = min(score_20, 30)

    # ===== 3️⃣ 趋势判断 =====
    ma20 = close.rolling(20).mean().iloc[-1]
    ma60 = close.rolling(60).mean().iloc[-1]
    score_trend = 10 if ma20 > ma60 else 0

    # ===== 4️⃣ 风险惩罚（短期大跌过滤） =====
    risk_penalty = 20 if ret_10 < -0.05 else 0

    # ===== 5️⃣ 总分 =====
    total_score = score_10 + score_20 + score_trend - risk_penalty
    total_score = max(0, round(total_score, 2))

    return {
        "total_score": total_score
    }
