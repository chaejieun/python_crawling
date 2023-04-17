from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%BD%94%EB%93%9C%EC%BF%A4%EC%8A%A4%ED%8A%B8"
browser = webdriver.Chrome("C:/Users/chaejieun/chromedriver.exe")
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 무한 스크롤 처리
# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤 
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h : 
        break
    before_h = after_h

# 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR,"._image._listImage")

for i, img in enumerate(imgs,1):
    # 각 이미지 태그의 주소
   img_src = img.get_attribute('src')
   print(i, img_src)
