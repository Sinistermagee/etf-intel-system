from modules.data_fetch import get_etf_data


ETF_POOL = ["510300", "510500", "159915", "512480"]


def calculate_all_scores():

    data = {}

    # ===== 1️⃣ 计算所有ETF的基础数据 =====
    for code in ETF_POOL:
        df = get_etf_data(code)
        if df is None or len(df) < 60:
            continue

        close = df["close"]

        ret_10 = (close.iloc[-1] - close.iloc[-11]) / close.iloc[-11]
        ret_20 = (close.iloc[-1] - close.iloc[-21]) / close.iloc[-21]

        ma20 = close.rolling(20).mean().iloc[-1]
        ma60 = close.rolling(60).mean().iloc[-1]

        data[code] = {
            "ret_10": ret_10,
            "ret_20": ret_20,
            "trend": ma20 > ma60
        }

    # ===== 2️⃣ 计算相对强度排名 =====
    ranked = sorted(data.items(), key=lambda x: x[1]["ret_10"], reverse=True)

    rank_score = {}
    for i, (code, _) in enumerate(ranked):
        if i == 0:
            rank_score[code] = 20
        elif i == 1:
            rank_score[code] = 10
        else:
            rank_score[code] = 0

    # ===== 3️⃣ 计算总分 =====
    results = {}

    for code, values in data.items():

        # 连续动量评分
        score_10 = max(0, values["ret_10"] * 800)
        score_10 = min(score_10, 40)

        score_20 = max(0, values["ret_20"] * 600)
        score_20 = min(score_20, 30)

        # 趋势过滤
        score_trend = 10 if values["trend"] else 0

        total_score = score_10 + score_20 + score_trend + rank_score.get(code, 0)

        results[code] = {
            "total_score": round(total_score, 2)
        }

    return results
