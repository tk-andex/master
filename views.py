from flask import render_template
from testapp import app

@app.route('/sampleform')
def sample_form():
    return render_template('testapp/sampleform.html')
    print('POSTデータ受け取ったので処理します')
    
    # フォームデータを取得
    data = request.form
    json_data = request.get_json()

    print("フォームデータ:", data)
    print("JSONデータ:", json_data)
    
    return 'POST受け取ったよ'

if __name__ == '__main__':
    app.run(debug=True)
