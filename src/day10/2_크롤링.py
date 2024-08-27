#2_크롤링.py

from bs4 import BeautifulSoup   #모듈 rkwudhrl
import urllib.request #

#[실습1] http://quotes.toscrape.com
url="http://quotes.toscrape.com" #크롤링할 url
response =urllib.request.urlopen(url) #지정한 url 요청
htmlData=response.read()#응답받은 내용물 전체 읽어오기
# print(htmlData)#확인
soup=BeautifulSoup(htmlData, "html.parser")#지정한 html문자열로  html 파싱객체 생성
# print(soup)#확인

#특정 마크업 /테크 파싱
quoteDivs= soup.select('.quote')
# print(quoteDivs)
for quote in quoteDivs:
    print(quote.select_one('.text').string)    #select는 리스트로 다 가져오고 select_one은 리스트아닌 하나씩 가져온다.
                                               #string은 글귀자체만 가져옴 ( 문자열 )
    #각 명언 저자 추출
    # print(quote.select('.author').string)

    # 각 명언 태그 추출
    tagDivs = soup.select('.tags')
    for tag in tagDivs:
        print(tag.select_one('.tag').string)

    # for tag in quote.select('.tag'):
    #     print(tag.string, end='\t')
    #각 명언 태그 목록 추출

#[실습2]
url="https://v.daum.net/v/20240827074833139"
response= urllib.request.urlopen(url)
htmlData=response.read()
soup=BeautifulSoup(htmlData,"html.parser")
 # print(soup)

#파싱하기
ps=soup.select('p')
# print(ps)
for p in ps:

    #본문 내용
    print(p.text)

#기사 제목
# print(soup.select_one('.tit_view').string)#[뉴스1 PICK]축구로 하나된 여야, 9월 정기국회 앞두고 '협치 다짐'
# print(soup.select_one('.news_view').text)

#[실습3]
url="https://search.naver.com/search.naver?query=%EB%B6%80%ED%8F%89%EA%B5%AC%EB%82%A0%EC%94%A8"
response=urllib.request.urlopen(url)
htmlData=response.read()
# print(htmlData)

soup=BeautifulSoup(htmlData,"html.parser")
# print(soup)

#온도
print(soup.select_one('.temperature_text').text)#현재 온도27.0°
print(soup.select_one('.summary_list').text)    #체감 28.3°   습도 68%   북풍 1.9m/s
print(soup.select_one('.summary_list').select('.sort')[1].text) #습도 68%









