import json

def lambda_handler(event, context):
    # イベントデータに基づいて処理を行う
    name = event.get("name", "Guest")
    age = event.get("age", "Unknown")

    # レスポンスを返す
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Hello, {name}! You are {age} years old.'
        })
    }