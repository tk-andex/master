from flask import Flask, request
app = Flask(__name__)

@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
    print('POSTデータ受け取ったので処理します')
    
    # フォームデータを取得
    data = request.form
    json_data = request.get_json()

    print("フォームデータ:", data)
    print("JSONデータ:", json_data)
    
    return 'POST受け取ったよ'

if __name__ == '__main__':
    app.run(debug=True)
