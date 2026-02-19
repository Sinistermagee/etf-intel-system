def sentiment_cap(sentiment):
    if "偏多" in sentiment:
        return 0.6
    elif "偏空" in sentiment:
        return 0.2
    else:
        return 0.4  # 中性


def base_position(score):
    if score >= 80:
        return 0.5
    elif score >= 70:
        return 0.3
    elif score >= 60:
        return 0.15
    else:
        return 0


def generate_recommendation(results, sentiment):
    message = "📊 ETF 智能轮动报告\n\n"
    message += sentiment + "\n\n"

    cap = sentiment_cap(sentiment)

    for i, item in enumerate(results[:3]):
        score = item["score"]
        theoretical_pos = base_position(score)

        final_pos = min(theoretical_pos, cap)

        if final_pos > 0:
            pos_text = f"建议仓位 {int(final_pos * 100)}%"
        else:
            pos_text = "观望"

        message += f"{i+1}️⃣ ETF {item['code']} 评分：{score} → {pos_text}\n"

    return message
