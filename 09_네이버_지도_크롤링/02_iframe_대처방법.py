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

# 가게 이름 10개 가져오기
names = browser.find_elements(By.CSS_SELECTOR, 'span.place_bluelink.TYaxT')
for name in names:
    print(name.text)