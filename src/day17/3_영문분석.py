#3_영문분석.py

#
import pandas as pd
import  glob
import re
from functools import  reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import  matplotlib.pyplot as plt
from wordcloud import  STOPWORDS , WordCloud


all_files=glob.glob('exportExcelData*.xls')

#pd 로 변환
all_files_data=[]
for file in all_files:
    # print(file)
    data_frame=pd.read_excel(file)  # xlrd 설치 설정가서 다운받아야됨
    all_files_data.append(data_frame)  #불러온 엑셀 df를 리스트에 담는다
# print(all_files_data)
#[3] 데이터프레임 합치기
all_files_data_concat=pd.concat(all_files_data, axis=0,ignore_index=True)

#[4]데이터프레임을 csv로 반환/내보내기
all_files_data_concat.to_csv('englishBigdata.csv',encoding='utf-8',index=False)

#(프로젝트 목표:학술문서의 제목분석) 데이터 전처리
#[5] 데이터프레임의 제목(열)만 추출
all_title=all_files_data_concat['제목']
# print(all_files_data_concat) 합침 확인
# 토큰화 준비 불용어 제거위해 목록 가져오기
영어불용어목록=stopwords.words('english')
# print(영어불용어목록)
표제어객체=WordNetLemmatizer() #영문 변형된 영문을 원형으로 다시  찾아주는 함수
# print(표제어객체)

#단어 토큰화
words=[]
for title in all_title:



