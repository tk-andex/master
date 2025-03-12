@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
    print('POSTデータ受け取ったので処理します')
    return 'POST受け取ったよ'
