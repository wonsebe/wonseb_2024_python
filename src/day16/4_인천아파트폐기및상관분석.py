#4_인천아파트폐기및상관분석.py

# [1] 가설 : 아파트 층과 건축년도 증가하면서 아파트 거래금액도 비싸다.
# [2] 주제: 아파트 층과 건축년도에 따른 거래금액 추이 비교 분석
# [3] 분석방법 : 다중 회귀분석, 상관분석
# 1. 데이터 수집
import pandas as pd
import seaborn as sns
data =pd.read_csv('아파트(매매)_실거래가_20240904134550.csv',encoding='cp949',skiprows=15, thousands=',')
    #thowsands=',' : 천단위 쉼표 생략 # 천단위를 정수타입으로 가져온다.

    #과제 : 해당 csv 파일을 분석하여 제출
print(data.isnull().sum())
data.info()

import matplotlib.pyplot as plt
import statsmodels.api as sm
others=list(set(data.columns).difference(set(["거래금액","intercept"])))
# p,resids=sm.graphics.plot_partregress("거래금액","intercept",others,data=data,ret_coords=True)
plt.title("인천광역시 아파트 회귀분석") #3. 차트 제목
plt.legend() #5. 차트 범례 표시
plt.show()  #6. 차트 보기








