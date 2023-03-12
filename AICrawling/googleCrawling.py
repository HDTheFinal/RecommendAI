from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
import shutil

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

def crawling_img(name, SEARCH_KEY):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('../chromedriver_win32', chrome_options=options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element("name", "q")
    elem.send_keys(SEARCH_KEY)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    scroll_count = 0
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
    # while scroll_count <= 5000:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
                scroll_count = scroll_count + 1
            except:
                break
        last_height = new_height

    imgs = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
    dir = "D:/coding/FINAL/RecommendAI/Recommend/test/"+ name

    createDirectory(dir) #폴더 생성
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,
                '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute("src")
            print(imgUrl)
            urllib.request.urlretrieve(imgUrl,  f"{dir}/{name}{str(count)}.jpg")
            count = count + 1
            if count >= 300000:
                break
        except:
            pass
    driver.close()

LOOKS = {
    # 'Chic' : '시크 룩',
    # 'Daily' : '데일리 룩',
    # 'Elegant' : '엘레강스 룩',
    # 'Formal' : '정장 룩',
    'Lovely' : '러블리 룩',
    'Modern' : '모던 룩'
}

for look in LOOKS.keys():
    # print(look, LOOKS[look])
    crawling_img(look, LOOKS[look])