#4_인천아파트폐기및상관분석.py

# [1] 가설 : 아파트 층과 건축년도 증가하면서 아파트 거래금액도 비싸다.
# [2] 주제: 아파트 층과 건축년도에 따른 거래금액 추이 비교 분석
# [3] 분석방법 : 다중 회귀분석, 상관분석
# 1. 데이터 수집
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
data =pd.read_csv('아파트(매매)_실거래가_20240904134550.csv',encoding='cp949',skiprows=15, thousands=',')
    #thowsands=',' : 천단위 쉼표 생략 # 천단위를 정수타입으로 가져온다.

    #과제 : 해당 csv 파일을 분석하여 제출
print(data.isnull().sum())
data.info()
print(data.describe())


print(data.value_counts())

회귀모형수식= '거래금액 ~  층+ 건축년도   ' #종속변수와 독립변수를 정의 # alcohol : 실제 wine 안에 있는 열 값을 가져옴 (맞춤법 틀리면 안됨)
선형회귀모델= ols(회귀모형수식, data= data)
선형회귀모델결과=선형회귀모델.fit()
print(선형회귀모델결과.summary())
# others=list(set(data.columns).difference(set(["거래금액","intercept"])))
# p,resids=sm.graphics.plot_partregress("거래금액","intercept",others,data=data,ret_coords=True)
# plt.title("인천광역시 아파트 회귀분석") #3. 차트 제목
# plt.show()  #6. 차트 보기
print(data['거래금액'].value_counts())
data['거래금액']=data['거래금액'].fillna('30000')
print(data['층'].value_counts())
data['층']=data['층'].fillna('30000')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(8,13))
sm.graphics.plot_partregress_grid(선형회귀모델결과,fig=fig)
plt.show()

data2=data.select_dtypes(include=[int,float,bool])
data_corr=data2.corr(method='pearson')
print(data_corr)
# data.to_csv('아파트상관계수표.csv',index=True)
data_corr.to_csv('아파트상관계수표.csv',index=True)

