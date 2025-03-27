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
    # "Authorization": "Bearer YOUR_id_token" ※access_tokenだと成功しない
    "Authorization": "Bearer eyJraWQiOiI4dDVvcEc0UVdRaERLZUN4cFwvMlh0Y1M2b2dUOHdvNDdFS0hBdWN3Wm0rND0iLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoidTdIVFFCX2djTXRJTnpFVktsM3hFdyIsInN1YiI6IjI3YTQ3YTM4LTEwYjEtNzBlMi1hMjVmLTNhYWE2YmE0MDgzMyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfaUNPN2VuOVkwIiwiY29nbml0bzp1c2VybmFtZSI6InRlc3QtdXNlcjIiLCJvcmlnaW5fanRpIjoiNzU0Y2IyNjEtMGVmMS00YTA2LWE5OGEtNTVmNWVmZThiOTgwIiwiYXVkIjoiNW02Njlyb2YwbjBta3BoMTVuM2ZoM3Y0cGUiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTc0MzA2MjUwMCwiZXhwIjoxNzQzMDY2MTAwLCJpYXQiOjE3NDMwNjI1MDAsImp0aSI6ImFjNDE1YzBhLTMyNDgtNGExOS1hOWY5LThkZTdkODM4YmY4NCIsImVtYWlsIjoiay50c3VrdWRhQGFuZC1leC5jby5qcCJ9.mj8LlWLBXCNaPbF4dN53f7sCMhKBJHd-wyYxTOyXZ7w7yLfZFSGkIIPNxm2CNGxxSPXFzjeAC0gTbY1PTQCTUGq2a-SYY0bps1rnlMt7DVzeDgAdHKdZremwRN6x3Ki_4KlyPnuwSvLAaBHGli3j7A05ZjLciFbwSc_Di0j6bbuqCECgqD5JJ0crH06wIZ-gypyy2mFEjGzrsnn47S1JDSn85Vych4Y2nN_QigqbZTiGISWpKiblJ6Pjt5o9SQL28Wvm4v5CGL92rw3YGFyeeUJ1oK_AbnvHrnjB_oM7rOD4kxeE0oJ56MyyvWOre2tcAvyBBnU-k9pzKPe_X7Rp5w",
    "Content-Type": "application/json"
}

# POSTリクエスト送信
response = requests.post(url, headers=headers, json=mydata)

# 結果を表示
print("Status Code:", response.status_code)
print("Response Body:", response.text)