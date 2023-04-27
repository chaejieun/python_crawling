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
