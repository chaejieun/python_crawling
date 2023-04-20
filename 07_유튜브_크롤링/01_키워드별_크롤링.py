from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요 >>>>")

# 브라우저 생성
browser = webdriver.Chrome('C:/Users/chaejieun/chromedriver.exe')
url = f"https://www.youtube.com/results?search_query={keyword}"
browser.implicitly_wait(10) # 로딩이 끝날 때 까지 10초까지는 기다려줌
browser.maximize_window
browser.get(url)

#  7번 스크롤하기
scroll_count = 7

i = 1
while True : 
    # 맨 아래로 스크롤을 내린다
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이에 페이지 로딩 시간 
    time.sleep(2)
    if i == scroll_count:
        break
    i += 1

# Selenium - Beautifulsoup 연동 방법
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')
infos = soup.select("div.text-wrapper")

for info in infos:
    # 원하는 정보 가져오기
    # 제목
    title = info.select_one("a#video-title").text

    try:
        # 조회수
        views = info.select_one("div#metadata-line > span:nth-of-type(1)").text

        # 날짜
        date = info.select_one("div#metadata-line > span:nth-of-type(2)").text
    except:
        views = "조회수 0회"
        date = "날짜 없음"

    print(title, views, date)