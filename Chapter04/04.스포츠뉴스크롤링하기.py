import requests
from bs4 import BeautifulSoup
import time


response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%86%90%ED%9D%A5%EB%AF%BC")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.select("div.info_group") # 뉴스 기사 div 10개 추출

for article in articles:
    links = article.select("a.info") # 리스트
    if len(links) >= 2 : # 링크가 2개 이상이면
        url = links[1].attrs['href'] # 두번째 링크의 href를 추출
        response = requests.get(url, headers={'User-agent':'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
 

        # 만약 연예 뉴스 라면
        if "entertain" in response.url :
            title = soup.select_one(".end_tit")
            content = soup.select_one("#articeBody")
        elif "sports" in response.url: 
            title = soup.select_one("h4.title")
            content = soup.select_one("#newsEndContents")

            # 본문 내용 안에 불필요한 div , p 삭제(compose)
            divs = content.select("div")     
            for div in divs :
                div.decompose() 
            paragraphs = content.select("p")
            for p in paragraphs:
                p.decompose()    
        else :
            title = soup.select_one("#title_area")
            content = soup.select_one("#contents")
        
        print("=========== 링크 ===========\n", url)
        print("=========== 제목 ===========\n", title.text.strip())
        print("=========== 본문 ===========\n", content.text.strip())
        time.sleep(0.3) # 프로그램을 0.3초 잠시 멈추게 함
        