import requests
from bs4 import BeautifulSoup

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

# 스크랩 준비
driver = webdriver.Chrome("../chromedriver_win32")

# txt 만들기 및 쓰기
currentLoc = 'C:/Users/KOSA/Desktop/THEFINAL/RecommendAI/TheHandsomeDB/PerfumeData/'
# perfume = open(currentLoc+'perfume.txt', 'w', encoding='utf-8')

# 크롤링 시작
url = 'https://www.perfumegraphy.com/category/genderless/661/?page=1'
driver.get(url)
time.sleep(1)

# 콘솔 초기화
os.system('cls')

# NOTE: PICK-UP 목록 (임의)
PICK_LOC = ['더현대대구', '본점', '판교', '신촌점']

CURRENT_CATEGORY = driver.current_url.split('/')[4]
resultText = open(currentLoc+'perfume_'+CURRENT_CATEGORY+'.txt', 'w', encoding='utf-8')

# 현재 카테고리 및 코드
CURRENT_CODE = CURRENT_CATEGORY[0:1].upper()

for page in range(100):
    print("--", driver.current_url)
    resultText.write(f"--{str(driver.current_url)}\n")
    wait = WebDriverWait(driver, 10)

    firstitem = '//*[@id="right"]/div[2]/div[2]/ul/li[1]'
    item = wait.until(EC.element_to_be_clickable((By.XPATH, firstitem)))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(2)

    # 상품 목록 ul
    itemlist = soup.select('ul.prdList>li.xans-record-')

    # 각 상품 정보 크롤링

    for idx, item in enumerate(itemlist):
        descSection = item.select_one('section.description')

        # NOTE: P_ID
        P_ID = item['data-product_no']
        # resultText.write(f"{str(CURRENT_CODE)}{str(P_ID)}\n")

        # NOTE: P_NAME
        P_NAME = descSection.select_one('strong.name>a').text
        # resultText.write(f"{str(P_NAME)}\n")

        # NOTE: P_BNAME
        P_BNAME = descSection.select_one('span.product-brand').text
        # resultText.write(f"{str(P_BNAME)}\n")

        # NOTE: 이미지1, 이미지 2
        P_IMAGE1 = item.select_one('section.thumbnail>a>img')['src']
        P_IMAGE2 = P_IMAGE1
        # resultText.write(f"{str(P_IMAGE1)}\n{str(P_IMAGE2)}\n")

        # NOTE: P_PRICE
        P_PRICE = descSection.select_one(
            'ul.spec>li.price>span').text.replace(',', '').replace('원', '')
        # resultText.write(f"{str(P_PRICE)}\n")

        # NOTE: P_DATE
        P_DATE = 'SYSDATE'

        # NOTE: P_LOC
        P_LOC = PICK_LOC[idx % 4]
        # resultText.write(f"{str(P_LOC)}\n")

        # NOTE: P_STOCK
        P_STOCK = 0
        # resultText.write(f"{str(P_STOCK)}\n")

        # NOTE: CATEGORY_CLARGE, CATEGORY_C_MEDIUM
        CATEGORY_CLARGE = '화장품'
        CATEGORY_C_MEDIUM = '향수/캔들'
        # resultText.write(f"{str(CATEGORY_CLARGE)} - {str(CATEGORY_C_MEDIUM)} \n")
        # resultText.write("\n")

        # TODO: P_LABEL
        P_LABEL = 'female|' + CURRENT_CATEGORY

        resultText.write(
            "insert into PRODUCT (P_ID,P_NAME,P_BNAME,P_IMAGE1,P_IMAGE2,P_PRICE,P_DATE,P_LOC,P_STOCK,CATEGORY_CLARGE,CATEGORY_C_MEDIUM,P_LABEL,P_BIMAGE)\n")
        resultText.write(
            f"values ('{str(CURRENT_CODE+P_ID)}','{str(P_NAME)}','{str(P_BNAME)}','{str(P_IMAGE1)}','{str(P_IMAGE2)}',{str(P_PRICE)},{str(P_DATE)},'{str(P_LOC)}',{str(P_STOCK)},'{str(CATEGORY_CLARGE)}','{str(CATEGORY_C_MEDIUM)}','{str(P_LABEL)}', NULL)\n\n")
    try:
        nextpage_btn = '//*[@id="right"]/div[3]/a[3]/img'
        driver.find_element(By.XPATH, nextpage_btn).click()
        time.sleep(2)
    except:
        print("데이터 수집 완료.")
        break

#     print('--------------------------------------------')
# 파일 닫기
resultText.close()
driver.close()
