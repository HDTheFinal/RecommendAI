from flask import Flask, request, json, jsonify
import requests
from keras.models import load_model
from Style_API.StylePredict import predict_custom_resnet50
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import shutil
import datetime

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


def getDate():
    nowDate = datetime.datetime.now().strftime("%Y/%m/%d")
    return nowDate

# FEAT: 디렉토리 생성
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
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

# FEAT: 이미지 업로드
@app.route("/uploadImg", methods=['POST'])
def upload_image():
    if request.method =='POST':
        f = request.files['file']

        save_dir ='C://dev64/upload/AItemp/' + getDate()
        print('dir: ' + save_dir)
        createDirectory(save_dir) #폴더 생성

        filePath = save_dir + '/' + secure_filename(f.filename)
        f.save(filePath);

        return filePath, 200
    

# FEAT: AI 분류 API
@app.route("/predict", methods=['POST'])
def get_predict():
    resnet50_model_path = 'PerfumeRecommend/Model/Recommend_with_resnet50_100epoch.h5'
    model = load_model(resnet50_model_path)
    
    data = request.json
    response = {
        'file' : data['file'],
    }
    result = predict_custom_resnet50(model, response['file'])

    return result, 200

# FEAT: API 실행
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)


