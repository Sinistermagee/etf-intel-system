from modules.data_fetch import get_etf_data
from modules.scoring import calculate_score
from modules.sentiment import get_market_sentiment
from modules.decision import generate_recommendation
from modules.feishu import send_feishu_message

ETF_POOL = [
    "510300",  # 沪深300
    "510500",  # 中证500
    "159915",  # 创业板
    "512480",  # 半导体
    "512170",  # 医疗
]

def main():
    results = []

    for code in ETF_POOL:
        df = get_etf_data(code)
        if df is None:
            continue

        score_detail = calculate_score(df)
        total_score = score_detail["total_score"]

        results.append({
            "code": code,
            "score": total_score
        })

    # 排序
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    sentiment = get_market_sentiment()

    message = generate_recommendation(results, sentiment)

    send_feishu_message(message)

if __name__ == "__main__":
    main()

