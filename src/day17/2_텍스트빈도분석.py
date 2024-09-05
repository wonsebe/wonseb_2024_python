#2_텍스트빈도분석.py

#1.분석할 텍스트 준비
textData = """Big data refers to the large volume of data – both structured and unstructured – that inundates a business on a day-to-day basis. 
But it’s not the amount of data that’s important. It’s what organizations do with the data that matters. 
Big data can be analyzed for insights that lead to better decisions and strategic business moves."""

#2. 다양한 전처리
    #(1) 정규화 : 모든 영대소문자를 소문자 변환
textData=textData.lower()
#"문자열".lower() : 소문자 변환 함수
#문자열".upper(): 대문자 로 변환 함수
print(textData)
    #(2) 정규화2: 구두점(.,?!:;'"() 등) 과 불필요한 특수문자/기호($_%*&) 제거     #정규표현식
import re   #정규표현식  #파이썬 내장 라이브러리
textData=re.sub(r'[^\w\s]','',textData)
print(textData)
    #\w: 문자 혹은 숫자   #\s: 공백(스페이스 바 , 탭키) / 띄어쓰기
    #^ : 부정     ^\w\s]: 문자 , 숫자 , 공백이 아닌것을 찾기
    #re.sub(r'정규표현식' , '대체문자' , ' 기존문자')    # 기존 문자열에서 정규표현식을 이용한 데이터를 찾아 대체하는 함수
        #(3) 문자열을 토큰(단어)화
words=textData.split(" ")
print(words)
#문자 개수 세기
from collections import  Counter    #컬렉션(리스트/딕셔너리/집합)
wordCount=Counter(words)
print(wordCount)    #중복된 요소들의 개수를 반환 해주는 함수

#4. 빈도가 높은 상위 n개만큼 출력 , most_common( N ) : 상위 N개 반환 해주는 함수
print(wordCount.most_common(10)) #제일많이 쓴 영문 10개만 선정해서 보여줌

#5. 시각화 : 워드클라우드
from wordcloud import  WordCloud
import matplotlib.pyplot as plt #시각화를 도와주는 모듈 (히스토그램 생성)

#(1) 워드클라우드 객체 생성  #WordCloud(width= 가로사이즈 , height=세로사이즈).generate(시각화할문자열)
wordcloud=WordCloud(width=800 , height=800, background_color='white').generate(textData)

#(2)
plt.imshow(wordcloud) #이거 꼭 넣어야됨 안하면 안보임
plt.axis('off') #x, y축 사라짐 (이미지만 남음 )
plt.show()
