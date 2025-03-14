from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONをASCIIエンコードしない

# データの仮置き
data = {"message": "こんにちは"}

# GETリクエストのエンドポイント
@app.route("/hello", methods=["GET"])
def get_hello():
    return jsonify(data)

# POSTリクエストのエンドポイント
@app.route("/hello", methods=["POST"])
def post_hello():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        return jsonify({"received": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
