# 향수 추천 AI

사진의 분위기에 따라 알맞은 향수를 추천해주는 AI

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

#### 1. 크롤링
1. 크롤링 환경 변수 생성
    1. `venv` 폴더를 생성한다.
    2. 가상 환경을 생성한다.
        ```
        // 가상환경 생성
        python -m venv crawling

        // 가상환경 활성화
        call crawling/Scripts/activate

        // 가상환경 종료
        deactivate
        ```
    3. 삭제할 시에는 폴더를 삭제한다.
2. 크롤링 모듈 설치
    ```
    // selenium
    pip install selenium

    // BeautifulSoup
    pip install bs4

    // requests
    pip install requests
    ```

#### 2. AI
1. 환경 변수 생성
    1. anaconda 설치 후, Environments를 생성 한다.
    2. 가상 환경의 폴더에 있는 python으로 interpreter를 변경한다.
    
2. AI 모듈 설치
    
    가상 환경 접속 후, `requirements.txt` 를 통해 설치한다.
    ```
    pip install -r requirements.txt
    ```
3. API 실행
    1. `app.py` 를 실행한다
    2. `/predict` 주소로 POST request를 전송한다.
        ```
        // json 형식으로 전송한다.
        {
            "file" : "<file path>"
        }
        ```


## Deployment

Add additional notes about how to deploy this on a live system

## Authors

* **박세영** *(Park Se Young)* - sy.park.HUB@gmail.com