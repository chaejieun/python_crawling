from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 브라우저 생성
browser = webdriver.Chrome('C:/Users/chaejieun/  chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) # 로딩이 끝날 때 까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, "a.nav.shop").click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)
