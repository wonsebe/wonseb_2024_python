#1_품사태깅.py

'''
    - 형태소: 의미가 있는 가장 작은 단위
    - 단어: 의미를 갖는 문장의 가장 작은 단일 요소, 문장내에서 분리 될 수 있는 부분 ,  #형태소 , 접사 구분
    - 품사 태깅: 형태소의 뜻과 문맥을 고려하여 품사를 붙인것
    - 품사 태깅 패키지 : konlpy( 자바 기반의 소프트웨어 , 자바 설치가 필요함 )
'''
#1.모듈 호출
from konlpy.tag import Okt  #설치해야됨 세빈아

#2. 분석할 한글
text= "나는 사과를 먹었다."

#3. 품사 태깅
    #3-1 . 품사 태깅 객체 생성
okt = Okt()
    #3-2. 품사 태깅 함수 실행   #okt.pos(분석할 문장)
tag_words=okt.pos(text)
#4. 확인
print(tag_words)
#[ ('나', 'Noun'), #Noun 명사

#예제2.
#2. 분석할 한글
text="""중·고등학생에서부터 젊은 직장인에게까지 1030세대를 중심으로 폭넓은 인기를 누려온 운동화 브랜드 '컨버스'가 휘청거리고 있다. 감성보다는 기능성을 중시한 '호카' 등의 브랜드가 인기몰이를 하면서 그 타격을 받은 것으로 풀이된다."""

#3. 품사태깅
okt = Okt()
#tag_words=okt.pos(text)
tag_words = okt.nouns(text) #.nouns() 명사 만 반환 함수

#4.확인
print(tag_words)
from collections import (Counter)
wordCount=Counter(tag_words)
print(wordCount)

#6. 특정 상위 N개 반환 함수
print(wordCount.most_common(3))

