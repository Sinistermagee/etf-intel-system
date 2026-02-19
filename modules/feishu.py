import os
import requests

FEISHU_WEBHOOK = os.getenv("FEISHU_WEBHOOK_URL")

def send_feishu_message(text):
    if not FEISHU_WEBHOOK:
        print("未配置飞书Webhook")
        return

    data = {
        "msg_type": "text",
        "content": {
            "text": text
        }
    }

    requests.post(FEISHU_WEBHOOK, json=data)
