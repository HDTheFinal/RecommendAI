from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import resnet50
import numpy as np

"""
 * StylePredict.py
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

def predict_custom_resnet50(model, filename) :
    # 이미지 전처리 및 삽입
    image = load_img(filename, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, 224, 224, 3))
    
    image = resnet50.preprocess_input(image)
    

    # 모델로 분류 및 최대 출력 인덱스 구하기
    yhat = model.predict(image)
    idx = np.argmax(yhat[0])

    result = {}

    # 커스텀 레이블과 각 분류 퍼센테이지 출력
    custom_labels = ['Daily', 'Formal', 'Lovely']

    for i, label in enumerate(custom_labels):
        print('%s (%.2f%%)' % (label, yhat[0][i]*100))
        result[label] = '%.2f' %  (yhat[0][i]*100)

    #최대 출력 인덱스 return
    return {'look' : custom_labels[idx], 
            'result' : result}