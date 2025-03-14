from pickle import FALSE
import requests
import json

# 送信先URL
# url = "http://127.0.0.1:5000/hello"
url = "https://doyv3lk5tj.execute-api.ap-northeast-1.amazonaws.com/lambda_function_API/"

# 送信するJSONデータ
data = {
    "queryStringParameters": {
        "param1": "Hello",
        "param2": "こんにちは"
    }
}

# ヘッダーの設定
headers = {
    "Content-Type": "application/json; charset=utf-8"
}

# POSTリクエストを送信
response = requests.post(url, json=data, headers=headers)
response.encoding = 'utf-8' # エンコーディングを指定(日本語の文字化け対応)

# レスポンスを表示
# print(url)
print("Status Code:", response.status_code)
print("Response Body:", response.text)
