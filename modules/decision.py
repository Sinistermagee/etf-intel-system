def generate_recommendation(results, sentiment):
    message = "📊 ETF 智能轮动报告\n\n"
    message += sentiment + "\n\n"

    for i, item in enumerate(results[:2]):
        message += f"{i+1}️⃣ ETF {item['code']} 评分：{item['score']}\n"

    return message
