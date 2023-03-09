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
resultText = open(currentLoc+'resultText.txt', 'w', encoding='utf-8')
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
for n in itemlist:
    print(n)
    print('--------------------------------------------')


# 파일 닫기
resultText.close()
driver.close()
