import requests
import os

FEISHU_WEBHOOK = os.getenv("FEISHU_WEBHOOK_URL")

def send_feishu_message(text):
    data = {
        "msg_type": "text",
        "content": {
            "text": f"ETF 智能策略日报\n\n{text}"
        }
    }

    response = requests.post(FEISHU_WEBHOOK, json=data)
    print("Feishu response:", response.text)
