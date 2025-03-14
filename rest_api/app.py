from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# 仮のデータ
tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Read a book", "done": True}
]

# すべてのタスクを取得するエンドポイント
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# IDで特定のタスクを取得するエンドポイント
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# 新しいタスクを追加するエンドポイント
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# タスクの完了ステータスを更新するエンドポイント
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)

# タスクを削除するエンドポイント
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

# アプリの実行
if __name__ == "__main__":
    app.run(debug=True)
