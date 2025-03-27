from pickle import FALSE
import requests
import json

# 送信先URL
# url = "http://127.0.0.1:5000/hello"
url = "https://doyv3lk5tj.execute-api.ap-northeast-1.amazonaws.com/lambda_function_API/"

# 送信するJSONデータ
# data = {
#     "queryStringParameters": {
#         "param1": "Hello",
#         "param2": "こんにちは"
#     }
# }

# 送信するJSONデータ(lambda)
data = {
  "resource": "/",
  "path": "/",
  "httpMethod": "POST",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiJZOW5aODhRb0hWSHR1cGJ6WWppQ3EwNlhGSG5nT2I4TmF0M1ZzRzZJSHpzPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI3N2U0ZWExOC0zMDQxLTcwNDItNTIzYy1mNjQ5YmE3MzFjYjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfWXNEZERvM2dsIiwiY2xpZW50X2lkIjoiMWdxb3VtdTNvdjh2bWkyNDRqaGVvYmM4YXYiLCJvcmlnaW5fanRpIjoiMDcxOWE0YzMtMjZhZS00MDE2LTlkNDgtNzk2MzE0NGFjYWY4IiwiZXZlbnRfaWQiOiJkYTU0NDBhZi0zZTczLTRjODQtYjRmMy02ODlkMTZiYWJiNDYiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNzQwOTkxNTczLCJleHAiOjE3NDA5OTUxNzMsImlhdCI6MTc0MDk5MTU3MywianRpIjoiMTg2ZDRhYjctZDNiMy00ZDAwLWE1NGYtOGRiOWY0MDM3ZWFmIiwidXNlcm5hbWUiOiJ0ZXN0LXVzZXIifQ.hnb9VBS_PvDaO-siyyz_fzazRB4ZHU5Z94VqaXQt7bJcPGqFQOntVy6vsHpbTOPJ30xOTFSXE1UFGm2n3UQ8Y32qDUOruBfHEchl7lMwjCnKiiLwdvvcR8v8Q_tVmM2rWOmRueKGUSF-gA-bxNYqjxZ0o6CReEQzq0jcQ5AQ1g0PCqy_WPQ9ycC-3QjxYXizQEmEvdb9CK01OWHe_-KMA3RqWwBWSKycv9RxWTcFrI8g7_Ea2wHmcovzXDdr5bWi8n8fijkv2O5bcV8o2BVLriCqAaDu2pXId4LcwcIVmWIoEXB_iCCphAEImbwo-z4VoKpUwOB-8yj9oLIPuFCsEQ"
  },
  "queryStringParameters": {
    "param1": "Hello",
    "param2": "こんにちは"
  },
  "pathParameters": {
    "id": "123"
  },
  "body": "{\"key\":\"value\"}",
#   "isBase64Encoded": false
}

# データをJSONに変換
# json_data = json.dumps(data)

# ヘッダーの設定
headers = {
    "Content-Type": "application/json; charset=utf-8"
}

# POSTリクエストを送信
response = requests.post(url, json=data, headers=headers)
response.encoding =  response.apparent_encoding # エンコーディングを指定(日本語の文字化け対応)

# レスポンスを表示
# print(url)
print("Status Code:", response.status_code)
print("Response Body:", response.text)
