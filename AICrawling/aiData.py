import os
import time
import urllib.request
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib3

driver = webdriver.Chrome()  # 크롬드라이버 설치한 경로 작성 필요
# 구글 이미지 검색 url
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q")  # 구글 검색창 선택
elem.send_keys('정장 룩')  # 검색창에 검색할 내용(name)넣기
elem.send_keys(Keys.RETURN)  # 검색할 내용을 넣고 enter를 치는것!

# 작게 뜬 이미지들 모두 선택(elements)
imgs = driver.find_elements(By.CSS_SELECTOR, ".wXeWr.islib.nfEiy")

img_folder = "C:/Users/KOSA/Desktop/THEFINAL/RecommendAI/AI_DataSet/Modern"  # 저장할 경로
count = 0

# 콘솔 초기화
os.system('cls')

# 폴더 삭제 후 실행
if os.path.isdir(img_folder):
    print('ㄴㄴ')
    os.rmdir(img_folder)
    os.mkdir(img_folder)
else:
    print('ㅇㅋ')
    os.mkdir(img_folder)


for img in imgs:
    img.click()
    time.sleep(2)

    # 크게 뜬 이미지 선택하여 "src" 속성을 받아옴
    imgUrl = driver.find_element(
        By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute("src")

    # NOTE: 해당 카테고리 이름 쓰기
    imgName = 'Modern'
    print(f'{imgUrl}/{imgName}{str(count)}.jpg')

    urllib.request.urlretrieve(imgUrl, f'{img_folder}/{imgName}{str(count)}.jpg')

    count = count + 1
    print(count)

    if count > 10:  # 다운 받을 이미지 갯수 조정
        break
