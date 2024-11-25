from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # CORS 임포트

app = Flask(__name__)
CORS(app)  # CORS 활성화

# 초기 하이스코어 설정
high_score = 10

# GET 요청 처리
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({"high_score": high_score})  # 하이스코어만 반환

# POST 요청 처리
@app.route('/send_data', methods=['POST'])
def send_data():
    global high_score
    received_data = request.json
    
    if 'score' in received_data:
        new_score = received_data['score']
        if new_score > high_score:
            high_score = new_score

    return jsonify({
        "received_data": received_data,
        "message": "Data received successfully",
        "new_high_score": high_score
    })

# HTML 페이지 제공
@app.route('/')
def index():
    return render_template('index.html')  # templates 폴더 내의 index.html 파일 제공

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


