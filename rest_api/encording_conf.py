import chardet

# ファイルのエンコーディングを確認する
with open('flask_api_endpoint.py', 'rb') as file:
    result = chardet.detect(file.read())
    print(result)