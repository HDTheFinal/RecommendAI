import requests
from bs4 import BeautifulSoup

import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

# 스크랩 준비
driver = webdriver.Chrome("../chromedriver_win32")
# txt 만들기 및 쓰기
currentLoc = 'C:/Users/KOSA/Desktop/THEFINAL/RecommendAI/TheHandsomeDB/'
# resultText.write('tttest');
# perfume = open(currentLoc+'perfume.txt', 'w', encoding='utf-8')

# 크롤링 시작
url = 'https://www.perfumegraphy.com/category/genderless/661/?page=1'
driver.get(url)
time.sleep(1)

# 콘솔 초기화
os.system('cls')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 상품 목록
itemlist = soup.select('ul.prdList>li.xans-record-')

# 각 아이템
# for n in itemlist:
#     print(n)
#     print('--------------------------------------------')

testItem = itemlist[0]

# P_ID
P_ID = testItem['data-product_no']

# 이미지1, 이미지 2
P_IMAGE1 = testItem.select_one('section.thumbnail>a>img')['src']
P_IMAGE2 = P_IMAGE1

# 설명란
descSection = testItem.select_one('section.description')

# P_BNAME
P_BNAME = descSection.select_one('span.product-brand').text

# P_NAME
P_NAME = descSection.select_one('strong.name>a').text

# P_PRICE
P_PRICE = descSection.select_one(
    'ul.spec>li.price>span').text.replace(',', '').replace('원', '')

with open(currentLoc+'resultText.txt', 'w', encoding='utf-8') as file:
    file.write(f"{str(P_ID)}\n")
    file.write(f"{str(P_IMAGE1)}\n{str(P_IMAGE2)}\n")
    file.write(f"{str(P_BNAME)}\n")
    file.write(f"{str(P_NAME)}\n")
    file.write(f"{str(P_PRICE)}\n")

# 파일 닫기
# resultText.close()
driver.close()
