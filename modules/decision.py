def position_advice(score):
    if score >= 80:
        return "建议仓位 50%"
    elif score >= 70:
        return "建议仓位 30%"
    elif score >= 60:
        return "建议仓位 15%"
    else:
        return "观望"


def generate_recommendation(results, sentiment):
    message = "📊 ETF 智能轮动报告\n\n"
    message += sentiment + "\n\n"

    for i, item in enumerate(results[:3]):
        advice = position_advice(item["score"])
        message += f"{i+1}️⃣ ETF {item['code']} 评分：{item['score']} → {advice}\n"

    return message
