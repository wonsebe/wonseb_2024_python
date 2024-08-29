#4_삼성전자시세정보.py

#실습1 :  삼성전자 의 최근 1년 시세 정보 CSV
    #1.데이터프레임 객체를 콘솔에 출력 (CSV -> 데이터프레임 )
    #2. 삼성전자의 최근 1년 시세 중 일자(X) 별 종가(Y)를 막대차트로 표현하시오
import pandas as pd
# 모듈 가져오기
import matplotlib
#pylot 모듈 가져오기
import matplotlib.pyplot as plt
try: pd=pd.read_csv('data_5524_20240829.csv')#
except Exception as e:
    pd=pd.read_csv('data_5524_20240829.csv',encoding='cp949'); print(pd)
# #1. 차트에 표시할 데이터 샘플 데이터 준비
# x=[]
# y=[]
# #2.라인플롯(선 차트)에 x축과 y축을 지정하여 라인플롯 생성
# plt.plot(x,y)
# plt.title('')
#3. 데이터 프레임의 특정 열 호출 #데이터 프레임 ['열이름']
print(pd['일자']) # 일자 열만 호출
print(pd['종가']) #종가 열만 호출


#4. 시각화 준비
import matplotlib.pyplot as plt
x=pd['일자']  #판다스 데이터프레임의 일자(열)을 x축
y=pd['종가']  #판다스 데이터프레임의 종가(열)를 y축
plt.plot(x,y)
plt.title('chart')
plt.xlabel('date')
plt.ylabel('price')
plt.show()












