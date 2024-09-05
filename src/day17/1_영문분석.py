#1_영문분석.py


import pandas as pd
import  glob
import  re
from functools import reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import  stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import  matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

#최초 1번만 실행
# import nltk
# nltk.download()

#[1] 여러개의 파일명을 불러오기
all_files=glob.glob('myCabinetExcelData*.xls')
    #*: 와일드카드: 모든 문자 대응 #myCabinetExcelData* : myCabinetExcelData 시작하는 파일명 검색
# print(all_files) 확인후 주석

#[2] 여러개 파일명에 해당하는 엑셀파일을 호출해서 pd로 변환하기  #엑셀파일 --> pd
all_files_data=[]
for file in all_files :     #모든 파일명을 하나씩 반복한다
    # print(file)
    data_frame=pd.read_excel(file)  #엑셀 모듈 : xlrd모듈 관련 오류 발생 # xlrd 설치 설정가서 다운받자 셉
    # print(data_frame)
    all_files_data.append(data_frame) #불러온 엑셀 df를 리스트에 담는다
# print(all_files_data)

#[3] 데이터프레임 합치기 #.concat(여러개프레임이저장된리스트,axis=0(세로 0,가로=1,ignore_index:인덱스 사용안함  )
all_files_data_concat=pd.concat(all_files_data, axis=0,ignore_index=True)
# print(all_files_data_concat)

#[4]데이터프레임을 csv로 반환/내보내기
all_files_data_concat.to_csv('riss_bigdata.csv',encoding='utf-8',index=False)

#(프로젝트 목표:학술문서의 제목분석)  데이터 전처리
#[5] 데이터프레임의 제목(열)만 추출
all_title=all_files_data_concat['제목']
# print(all_title)

#[6] 단어 토큰화 준비 stopwords.words('') : 영어 불용어 목록 가져오는 함수
# #WordNetLemmatizer(): 표제어 추출기 객체 생성
    #표제어: 단어의 원형(기본형)찾는 과정 즉, 영문 변형된 영문을 원형으로 다시  찾아주는 함수 # 시제 , 단/복수 진행어 등등 일반화 과정
영문불용어목록=stopwords.words('english')
# print(영문불용어목록)
표제어객체=WordNetLemmatizer()

#[7] 단어 토큰화
words=[]
for title in all_title: # 제목 목록에서 제목 하나씩 반복하기
    # print(title)
    #7-1 영문이 아닌것을 정규표현식을 이용해서 치환
    EnWords=re.sub(r'[^a-zA-Z]+'," ",str(title))
    # print(EnWords)

    #7-2 소문자로 변환하고 토큰화  word_tokenize(문자열) #지정한 문자열을 토큰(단어) 추출하여 리스트로 변환
    EnWordsToken=word_tokenize(EnWords.lower())
    # print(EnWordsToken)

    #7-3 불용어 제거(해당 토큰(단어) 리스트에 불용어가 포함되어 있으면 제거 )   #반복문을 이용한 조건에 따른 새로운 리스트 생성
        #리스트 컴프리헨션 사용x
    # EnWordsTokenShop=[] #불용어가 제거된 토큰들 저장하는 리스트
    # for w in EnWordsToken :
    #     if w not in 영문불용어목록 :   #해당 단어가 불용어목록에 포함이 아니면
    #         EnWordsToken.append(w)
        #리스트 컴프리헨션 사용0
    EnWordsTokenShop=[w for w in EnWordsToken if w not in 영문불용어목록]
        # if 값 in 리스트: 리스트내 해당 값이 존재하면 true 아니면 false
        # if 값 not in 리스트 : 리스트내 해당 값이 존재하면 false 아니면 true

    #7-4 표제어 추출
    #리스트 컴프리헨션 사용0 #표제어객체.lemmatize(단어) #단어에서 시제, 단/복수, 진행형 들을 일반화 단어로 추출
    EnWordsTokenShopLemma=[표제어객체.lemmatize(w) for w in EnWordsTokenShop]
    # 리스트 컴프리헨션 사용x
    EnWordsTokenShopLemma = []
    for w in EnWordsTokenShop:#불용어가 제거된 리스트에서 표제어 추출
        EnWordsTokenShopLemma.append(표제어객체.lemmatize(w))

        # print(EnWordsTokenShopLemma)
    words.append(EnWordsTokenShopLemma) # 제목을 정규화 -> 토큰화 -> 불용어제거 -> 표제어추출한 결과를 리스트에 담기
#반복문 종료
# print(words)

#[8] 2차원 리스트를 1차원 변환    #Counter는 1차원 밖에 못 센다... #reduce(람다식함수 , 2차원 테스트)
    #reduce 사용0 이번시간에 제일 중요한부분!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    words2=reduce(lambda x,y: x+y, words)
    # print(words2)

# #파이썬 람다식  #lambda 매개변수1, 매개변수2 : 실행문
#     #매개변수의 제곱을 하는 함수를 람다식 표현
# 제곱함수=lambda x: x**2
# print(제곱함수(1))
# print(제곱함수(2))
#     #람다식이 아닌 일반 함수
# def 제곱함수2(x):
#     return x ** 2
# print(제곱함수2)


    #reduce 사용x
# words2=[]
# for w in words:
#     words2.extend(w) #리스트1.extend(리스트2) #.extend() 두 리스트를 하나의 리스트로 반환 함수

# print(words2)

#(9)리스트내 요소 개수 세기 ( 단어 빈도 구하기 ) #리스트내 요소들의 빈도 수를 튜플로 해서 여러 튜플을 리스트로 반환해준다.
count=Counter(words2)
# print(count)

#[10] 빈도가 높은것만 추출
# print(count.most_common(50))
word_count=dict()   #빈 딕셔너리 생성
for (tag,counts) in count.most_common(50):
    print(tag,counts)
    if(len(tag)>1): #만약에 단어가 1보다 작으면 제외
        word_count[tag]=counts
print(word_count)

# #히스토그램
# sorted_keys=sorted(word_count,key=word_count.get,reverse=True)
# sorted_Values=sorted(word_count.values(),reverse=True)
# plt.bar(range(len(word_count)),sorted_Values,align='center')
# plt.xticks(range(len(word_count)),list(sorted_keys),rotation='vertical')
# plt.show()

#딕셔너리.keys() : 딕셔너리내 모든 key값 호출 반환, 딕셔너리.keys(): 딕셔너리 모든 value값 호출 반환,
# plt.bar(word_count.keys(),word_count.values(), 'center')

#딕셔너리 정렬방법
sorted_keys=sorted(word_count, key=word_count.get,reverse=True)
            #key = word_count.get 은 get 메소드를 참조해 각키를 value(빈도수) 기준으로 정렬
            #reverse : 내림차순 가능 생략시 오름차순
sorted_Values=sorted(word_count.values(),reverse=True)
# print(sorted_keys)

# print(range(len(word_count))) #range(0,50) : 0부터 49
plt.bar(range(len(word_count)),sorted_Values)
plt.xticks(range(len(word_count)),list(sorted_keys),rotation=85)
    #x축에 단어(keys)들 , y축 단어빈도수(values)들
# print(range)
plt.show()

all_files_data_concat['doc_count']=0    #데이터프레임 필드(열) 추가
    #출판일 별로 'doc_count'의 기술통계
summary_year=all_files_data_concat.groupby('출판일',as_index=False)['doc_count'].count()
    # 데이터프레임 에서 '출판일' 열 기준으로 그룹화하고
    # as_index=False 그룹화 할 때 인덱스는 제외
    #.count() : 행 개수
# print(summary_year)
plt.figure(figsize=(12,5))
plt.xlabel("year")
plt.ylabel('doc_count')
plt.grid(True)
plt.plot(range(len(summary_year)),summary_year['doc_count'])
plt.xticks(range(len(summary_year)),[text for text in summary_year['출판일']])
plt.show()

    #[13]워드 클라우드
        #(1) 문자열타입의 텍스트들의 워드 클라우드
    #wc=WordCloud.generate("문자열타입")
        #(2)딕셔너리타입의 텍스트들의 워드 클라우드
    #wc=WordCloud().generate_from_frequencies("딕셔너리타입")
stopwords=set(STOPWORDS)
wc=WordCloud(background_color='ivory',stopwords=stopwords,width=800,height=600)
cloud=wc.generate_from_frequencies(word_count)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()


wc=WordCloud().generate_from_frequencies(word_count)
plt.imshow(wc)
plt.show()
wc.to_file("wordCloud.jpg")