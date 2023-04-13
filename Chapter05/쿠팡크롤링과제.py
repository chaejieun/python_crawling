import requests
from bs4 import BeautifulSoup
import time
import pyautogui

# 입력
keyword = pyautogui.prompt("검색어를 입력하세요")

response = requests.get(f"https://www.coupang.com/np/search?component=&q={keyword}&channel=user")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
products = soup.select(".search-product")
print(products)

# for product in products:
#     url = product.select("a.search-product-link").attrs['href']
#     response = requests.get(url, headers={'User-agent':'Mozila/5.0'})
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     brand = soup.select_one("a.prod-brand-name")
#     print(brand)
#     time.sleep(0.3)
