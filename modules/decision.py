import math


def generate_recommendation(results, sentiment):

    message = "📊 ETF 智能轮动报告\n\n"
    message += sentiment + "\n\n"

    risk_off = "Risk Off" in sentiment
    max_total_position = 50  # 总仓位上限

    positions = []

    # ===== 1️⃣ 初始仓位计算 =====
    for item in results[:3]:
        score = item["score"]

        if score >= 70:
            position = 30
        elif score >= 60:
            position = 20
        else:
            position = 0

        if risk_off and position > 0:
            position = position * 0.5

        positions.append(position)

    # ===== 2️⃣ 总仓位控制 =====
    total_position = sum(positions)

    if total_position > max_total_position:
        scale = max_total_position / total_position
        positions = [p * scale for p in positions]

    # ===== 3️⃣ 向下取整到5% =====
    positions = [math.floor(p / 5) * 5 for p in positions]

    # ===== 4️⃣ 输出 =====
    for i, item in enumerate(results[:3]):
        score = item["score"]
        position = positions[i]

        if position > 0:
            message += f"{i+1}️⃣ ETF {item['code']} 评分：{score} → 建议仓位 {position}%\n"
        else:
            message += f"{i+1}️⃣ ETF {item['code']} 评分：{score} → 观望\n"

    return message
