import requests
from bs4 import BeautifulSoup

#naver 서버 requests
response = requests.get("https://www.naver.com/")

#naver에서 html response
html = response.text

#html을 가지고 soup 생성
soup = BeautifulSoup(html, 'html.parser')

#id 값이 NM_set_home_btn을 조회
word = soup.select_one('#NM_set_home_btn')

# text 요소 출력
print(word.text)