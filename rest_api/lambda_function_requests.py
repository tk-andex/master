import requests
import json

# 送信するデータ
# operation = "PUT"
# data = {"temp": 28.0, "humid": 60}

# payload = json.dumps({
#     "message": f"Received operation: {operation}",
#     "data": data
# }, ensure_ascii=False)

# 送信するJSONデータ(lambda)
data = {
  "operation": "PUT",
  "data": {
      "en": "Hello",
      "jp": "こんにちは"
  }
}

# APIのURL (テスト用に変更してください)
url = "https://doyv3lk5tj.execute-api.ap-northeast-1.amazonaws.com/lambda_function_API"

# ヘッダー設定 (JSONデータを送ることを明示)
headers = {"Content-Type": "application/json"}

# POSTリクエスト送信
response = requests.post(url, json=data, headers=headers)

# 結果を表示
print("Status Code:", response.status_code)
print("Response Body:", response.text)