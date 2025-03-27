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
    "Authorization": "Bearer eyJraWQiOiI4dDVvcEc0UVdRaERLZUN4cFwvMlh0Y1M2b2dUOHdvNDdFS0hBdWN3Wm0rND0iLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoiQURGUFd0X2FiVXR2VHB0a0RxNzJzZyIsInN1YiI6IjI3YTQ3YTM4LTEwYjEtNzBlMi1hMjVmLTNhYWE2YmE0MDgzMyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfaUNPN2VuOVkwIiwiY29nbml0bzp1c2VybmFtZSI6InRlc3QtdXNlcjIiLCJvcmlnaW5fanRpIjoiYmJlYzA5NDItOTBhNC00ZDUyLTkxMWMtZTg1OTg3ZTQzOGRjIiwiYXVkIjoiNW02Njlyb2YwbjBta3BoMTVuM2ZoM3Y0cGUiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTc0MzA2NzExOCwiZXhwIjoxNzQzMDcwNzE4LCJpYXQiOjE3NDMwNjcxMTgsImp0aSI6IjY4OTEwZWRjLTc3NWQtNGNhNC1hMmM2LTY1YTg3MDVjNzJkZSIsImVtYWlsIjoiay50c3VrdWRhQGFuZC1leC5jby5qcCJ9.TGhFZ92-cgf35WFqzJ4bze8tTA77R2ZXJlZJgp_aYvbf0P9Dd9uB4BvhfHFnqyhKLMEwOBDFJJfuZv0lulbg7vcr9vSUtpapn_2rkOPYFU92o5Rd4WwpjvzHM1x6iDtSRzhmu5HyySrp0PAccicXEThn8iC8noGBM87ZlGkzPpR9AY1XkGKy9KBf9NaCkv7fZTnKE5xpiIMeMN1kX6rlL3mdFjvniDtWdoBVwb-5_EN8XoDGymK-QI-9RYxJLa5MngvYSWWKYbYn5az6QuKTKnz_Y_TqEX5fzljyT-zF-zo-pQts30WaKZ9T2wKl59_8eEA-3xsRSNVMMjQk4Bd8uQ",
    "Content-Type": "application/json"
}

# POSTリクエスト送信
response = requests.post(url, headers=headers, json=mydata)

# 結果を表示
print("Status Code:", response.status_code)
print("Response Body:", response.text)