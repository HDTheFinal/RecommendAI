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

<!-- End with an example of getting some data out of the system or using it for a little demo -->

## Deployment

Add additional notes about how to deploy this on a live system

## Authors

* **박세영** *(Park Se Young)* - sy.park.HUB@gmail.com