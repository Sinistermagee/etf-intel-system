def generate_recommendation(results, sentiment):

    message = "📊 ETF 智能轮动报告\n\n"
    message += sentiment + "\n\n"

    risk_off = "Risk Off" in sentiment

    for i, item in enumerate(results[:3]):
        score = item["score"]

        if score >= 70:
            position = 30
        elif score >= 60:
            position = 20
        else:
            position = 0

        # 如果 Risk Off，仓位减半
        if risk_off and position > 0:
            position = position / 2

        if position > 0:
            message += f"{i+1}️⃣ ETF {item['code']} 评分：{score} → 建议仓位 {position}%\n"
        else:
            message += f"{i+1}️⃣ ETF {item['code']} 评分：{score} → 观望\n"

    return message
