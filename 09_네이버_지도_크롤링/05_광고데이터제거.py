import requests
from bs4 import BeautifulSoup
import pyautogui
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


url = f"https://map.naver.com/v5/"

browser = webdriver.Chrome("C:/Users/chaejieun/chromedriver.exe")
browser.get(url)
browser.implicitly_wait(10)
browser.maximize_window

# 검색창 입력
search = browser.find_element(By.CSS_SELECTOR, "input.input_search")
search.click()
time.sleep(1)
search.send_keys('대흥역 맛집')
time.sleep(1)
search.send_keys(Keys.ENTER)

# iframe 안으로 들어가기
browser.switch_to.frame("searchIframe")

# browser.switch_to_default_content() iframe 밖으로 나오기


# iframe 안쪽을 한번 클릭하기
browser.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click()

# 로딩된 데이터 개수 가져오기
lis = browser.find_elements(By.CSS_SELECTOR, "li.UEzoS")
before_len = len(lis)

while True:
    # 맨 아래로 스크롤 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1.5)

    # 스크롤 후 로딩된 데이터 개수 확인
    lis = browser.find_elements(By.CSS_SELECTOR, "li.UEzoS")
    after_len = len(lis)

    # 로딩된 데이터 개수가 같다면 반복 멈춤
    if before_len == after_len:
        break
    before_len = after_len

# 데이터 기다리는 시간을 0으로 만들어줌 (데이터가 없더라도 빠르게 넘어감)
browser.implicitly_wait(0)

for li in lis:
    # 광고 상품 아닌 것만
    if len(li.find_elements(By.CSS_SELECTOR, "svg.dPXjn")) == 0 :
        # 별점이 있는 것만 크롤링
        if len(browser.find_elements(By.CSS_SELECTOR, "span.h69bs.a2RFq")) > 0 :
            # 가게명
            try:
                name = li.find_element(By.CSS_SELECTOR, "span.place_bluelink.TYaxT").text
            except:
                name = "0"
            # 별점
            try:
                star = li.find_element(By.CSS_SELECTOR, "span.h69bs.a2RFq > span").text
            except: "0"

            # 영업 시간이 있다면
            if len(li.find_elements(By.CSS_SELECTOR, "span.h69bs.KvAhC")) > 0 :
                # 리뷰수
                try:
                    review = li.find_element(By.CSS_SELECTOR, "span.h69bs:nth-child(3)").text
                except:
                    review = "0"
        # 영업 시간이 없다면
        else :
            try:
                review = li.find_element(By.CSS_SELECTOR, "span.h69bs:nth-child(2)").text
            except:
                review = "0"

        print(name, star , review )
