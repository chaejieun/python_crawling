from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request
import pyautogui




keyword = pyautogui.prompt("검색어를 입력하세요 >>> ")

if not os.path.exists(f"06_구글_이미지_크롤링/{keyword}"):
    os.mkdir(f'06_구글_이미지_크롤링/{keyword}')


url = f"https://www.google.com/search?q={keyword}&hl=ko&source=lnms&tbm=isch&sa=X&ved=2ahUKEwik-_qd3bP-AhXOslYBHQV_D1UQ_AUoAXoECDEQAw&biw=2844&bih=1432&dpr=1.35"
browser = webdriver.Chrome("C:/Users/chaejieun/chromedriver.exe")
browser.implicitly_wait(10)
browser.maximize_window
browser.get(url)

before_h = browser.execute_script("return window.scrollY")

while True :
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1)
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h :
        break
    before_h = after_h

# 썸네일 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")

for i, img in enumerate(imgs, 1):
    # 이미지를 클릭해서 큰 사이를 찾음
    # 클릭하다보면 element click intercepted 에러 발생
    # javascript로 클릭을 직접 하도록 만들어주면 됨 
    browser.execute_script("arguments[0].click();",img)
    #img.click()
    time.sleep(1)

    # 큰 이미지 주소 추출
    if i == 1:
        target = browser.find_elements(By.CSS_SELECTOR, "img.r48jcc.pT0Scc.iPVvYb")[0]
    else:
        target = browser.find_elements(By.CSS_SELECTOR, "img.r48jcc.pT0Scc.iPVvYb")[1]

    img_src = target.get_attribute('src')

    # 이미지 다운로드
    # 크롤링 하다보면 HTTP Error 403: Forbidden 에러 발생 
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozila/5.0')]
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(img_src, f'06_구글_이미지_크롤링/{keyword}/{i}.jpg')
    except:
        pass