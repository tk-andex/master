# /////////////////////////////
# pythonでjson読込基本
# ////////////////////////////

# jsonをインポート
import json

# データ
# data = {
#     "section1":{
#         "key":"リンゴ",
#         "number": 1
#     },

#     "section2":{
#         "key":"みかん",
#         "number": 2
#     }
# }

# with open('読み込みたいファイル', 'r')  // rはread、 encoding="utf-8"は日本語文字化対応、json.loadでデコード
with open('sample.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

# 変数B = json.loadとはデコード（元に戻す）
# json_load = json.load(json_open)

# データをjson.dumpsでJSON形式にエンコード変換 ensure_asciiは日本語文字化け対応
# json_data = json.dumps(json_open, indent=2, ensure_ascii=False)

# jsonを表示
# print(data, end='\n')


# forでjsonからデータ抽出 
for j in data.values():
    print(j['key'])