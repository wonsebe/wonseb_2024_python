#4_한글기사.py
import re
# 주제: 다음 경제 뉴스의 최신 10페이지 기사들 제목의 단어 빈도수 분석
import urllib.request
from bs4 import BeautifulSoup
#1.데이터 준비
textData=[]
for page in range(1,11):
    url="https://news.daum.net/breakingnews/economic?page={page}"
    response=urllib.request.urlopen(url)
    htmlData=response.read()
    soup=BeautifulSoup(htmlData,"html.parser")
    list_news2 =soup.select_one('.list_news2 ')
    # print(list_news2)
    for li in list_news2.select('li'):
        # print(list_news2)
        title=li.select_one('.tit_thumb> a').string
        textData.append(title) #7. 기사 제목을 리스트에 담기

#2. 품사 태깅
    #1. 정규표현식
message=''
for msg in textData:
    message+=re.sub(r'[^\w]','',msg)
    #2. 태깅
from konlpy.tag import Okt
okt=Okt()
words=okt.nouns(message)
# print(words)
#3. 분석 (빈도수)
from collections import Counter
wordCount=Counter(words)
    #2. 상위 N개 추출
bestWords=wordCount.most_common(30)

    #딕셔너리 변환
wordDict={}
for word,count in bestWords:
    if len(word) >1:
        wordDict[word]=count


#4. 시각화 ( 히스토그램 , 워드클라우드 )

from wordcloud import  WordCloud
import matplotlib.pyplot as plt
wc= WordCloud("c:/windows/fonts/malgun.ttf").generate_from_frequencies(wordDict)
#4. 시각화(히스토그램, 워드 클라우드)
plt.imshow(wc)
plt.show()




