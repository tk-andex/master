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
mydata = {
  "operation": "PUT",
  "data": {
      "en": "Hello",
      "jp": "こんにちは"
  }
}

# APIのURL (テスト用に変更してください)
url = "https://doyv3lk5tj.execute-api.ap-northeast-1.amazonaws.com/lambda_function_API"

# ヘッダー設定 (JSONデータを送ることを明示)
headers = {
    # "Authorization": "Bearer YOUR_id_token"=JWT ※access_tokenだと成功しない
    "Authorization": "Bearer eyJraWQiOiI4dDVvcEc0UVdRaERLZUN4cFwvMlh0Y1M2b2dUOHdvNDdFS0hBdWN3Wm0rND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIyN2E0N2EzOC0xMGIxLTcwZTItYTI1Zi0zYWFhNmJhNDA4MzMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb21cL2FwLW5vcnRoZWFzdC0xX2lDTzdlbjlZMCIsImNvZ25pdG86dXNlcm5hbWUiOiJ0ZXN0LXVzZXIyIiwib3JpZ2luX2p0aSI6IjU4OGY1NmNlLWZkMzItNDQxYy1hMmEwLTA2NTljMzViMWQ0YiIsImF1ZCI6IjVtNjY5cm9mMG4wbWtwaDE1bjNmaDN2NHBlIiwiZXZlbnRfaWQiOiIzMmRjMzU4Ny02ZmI3LTQ1NjAtYjAxZC1lNmI4NDljNzk3MjMiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTc0MzE0Mzk3NSwiZXhwIjoxNzQzMTQ3NTc1LCJpYXQiOjE3NDMxNDM5NzUsImp0aSI6ImM0MDE1ZWM3LTg0ODgtNDY0MC1iOTlhLTM3MjFkOTNiYjhiNSIsImVtYWlsIjoiay50c3VrdWRhQGFuZC1leC5jby5qcCJ9.XjdImhqC_zjCm0CzwMBFJNS3nTQvsgf6kOF_uvXLeDmZ55trd4TDNUmWstsjxk6yF6-rHgfJAGyoJuN8Y3ZVVLT22WL2PdE-sUHoU6AUpJn9secsVEJNKp-TPo_Us3xRXQTziN-fH5eG6HNMuq-71clgzoLgbFtGIa2i2nyv5FTJU3HLoePJgkZjX5qho4lnSDMYVX5qej7PBd6OIGCVTyb_-ziz0E1-dl3_V-HDHy6WoiHAdheKWd9sUW8PTfC5FC1dpqcmWRvuMy9hYx-A5oQ5zIJNx_oQabF0Ygca0sjevC7wuozr2zCFQ9P9THy0ylimnD0a7vvw2mJZgar1MQ",
    "Content-Type": "application/json"
}

# POSTリクエスト送信
response = requests.post(url, headers=headers, json=mydata)

# 結果を表示
print("Status Code:", response.status_code)
print("Response Body:", response.text)