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
    data_frame=pd.read_excel(file)
    all_files_data.append(data_frame)
# print(all_files_data)
all_files_data_concat=pd.concat(all_files_data, axis=0,ignore_index=True)