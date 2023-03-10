import os
import time
import urllib.request
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import shutil

# 콘솔 초기화
os.system('cls')

# FEAT: 폴더 삭제 후 실행
img_folder = "C:/Users/KOSA/Desktop/THEFINAL/RecommendAI/AI_DataSet/Modern"

if os.path.isdir(img_folder):
    print('존재O')
    shutil.rmtree(img_folder)
    os.mkdir(img_folder)
else:
    print('존재X')
    os.mkdir(img_folder)

# FEAT: 이미지크롤링
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q")  # 구글 검색창 선택
elem.send_keys('정장 룩')  # 검색창에 검색할 내용(name)넣기
elem.send_keys(Keys.RETURN)  # 검색할 내용을 넣고 enter를 치는것!

#
SCROLL_PAUSE_TIME = 1
scroll_count = 0
# Get scroll height
last_height = driver.execute_script(
    "return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음

# NOTE: 스크롤 할 횟수 쓰기
while scroll_count > 10:
    # Scroll down to bottom
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

# 작게 뜬 이미지들 모두 선택(elements)
imgs = driver.find_elements(By.CSS_SELECTOR, ".wXeWr.islib.nfEiy")
count = 0

for img in imgs:
    try:
        img.click()
        time.sleep(2)

        # 크게 뜬 이미지 선택하여 "src" 속성을 받아옴
        imgUrl = driver.find_element(
            By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute("src")

        # NOTE: 해당 카테고리 이름 쓰기
        imgName = 'Modern'
        print(f'{imgUrl}/{imgName}{str(count)}.jpg')

        urllib.request.urlretrieve(
            imgUrl, f'{img_folder}/{imgName}{str(count)}.jpg')

        count = count + 1
        print(count)

        if count > 100000:  # 다운 받을 이미지 갯수 조정
            break
    except:
        pass

driver.close()
