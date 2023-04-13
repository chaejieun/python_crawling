import requests
from bs4 import BeautifulSoup
import time
import pyautogui

# 입력
keyword = pyautogui.prompt("검색어를 입력하세요")
header = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',}

response = requests.get(f"https://www.coupang.com/np/search?component=&q={keyword}&channel=user",headers=header)
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
