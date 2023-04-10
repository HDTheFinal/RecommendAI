from flask import Flask, request, json, jsonify
import requests
from keras.models import load_model
from Style_API.StylePredict import predict_custom_resnet50
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

"""
 * StrylePredict.py
 * @author SeyoungPark
 * @since 2023. 3. 14.
 *  <pre>
 * 수정일        	수정자       		수정내용
 * ------------    -----------    ---------------------------
 * 2023. 3. 14.   SeyoungPark     최초 생성
 * 2023. 3. 24.   SeyoungPark     API 결과 (text -> json) 변경 및 함수 분리
 * </pre>
 */
"""

import os
import shutil

# FEAT: 디렉토리 생성
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print('존재O')
            shutil.rmtree(directory)
            os.mkdir(directory)
    except OSError:
        print("Error: Failed to create the directory.")

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# FEAT: GET-서버 테스트용 API
@app.route("/enter", methods=['GET'])
def test_enter():
    return "enter"

# FEAT: AI 분류 API
@app.route("/predict", methods=['POST'])
def get_predict():
    resnet50_model_path = 'PerfumeRecommend/Model/Recommend_with_resnet50_100epoch.h5'
    model = load_model(resnet50_model_path)
    
    data = request.json
    response = {
        'file' : data['file'],
    }
    print(response)
    result = predict_custom_resnet50(model, response['file'])
    print(result)

    return result, 200

# FEAT: API 실행
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)


