#1_주택가격분석.py


import  pandas as pd
# from sklearn.datasets import  load_boston
# #보스턴 주택 데이터 가졍괴     #sklearn 1.2 이후 제공하지않아서 오류남
# boston=load_boston()
# print(boston)
'''import pandas as pd
    import numpy as np

    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
''' #이거 복사해서 사용하자

#보스턴 주택데이터 가져오기
import pandas as pd
import numpy as np
data_url = "http://lib.stat.cmu.edu/datasets/boston" #보스턴 주택 정보가 있는 url
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None) #해당 url 가져오기
    #지정한 url 에서 데이터를 데이터프레임으로 가져오기
    #sep="\s+" : 데이터 간의 공백으로 구분된 csv
    #skiprows=22: 위에서부터 22행까지 생략
    # header=None: 헤더가 없다는 뜻
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
# print(data.shape) #주택관련변수들 ( 독립변수 ,피처 )
target = raw_df.values[1::2, 2]
# print(target.shape)   #주택가격 ( 종속변수 , 타깃변수 )

#독립변수의 이름
feature_names = ['CRIM', 'ZN', 'INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
#데이터 프레임 생성     #독립변수 데이터와 독립변수의 이름 으로 데이터프레임 생성
boston_df=pd.DataFrame(data, columns=feature_names )
# print(boston_df.head())
#4. 데이터 프레임의 주택가격 열 추가
boston_df['PRICE'] = target
# print(boston_df.head())
# print('보스턴 주택 가격 데이터셋 크기: ', boston_df.shape)
# print(boston_df.info()) #열이름 , 열의 데이터수, 데이터타입, 메모리
#===========================[2] 분석 모덱 구축===================================#
#1. 타겟과 피처 분할하기
Y=boston_df['PRICE'] #종속변수 , 타겟
X=boston_df.drop('PRICE', axis=1, inplace=False) #독립변수 , 피처 #주택가격 외 정보
#2. 훈련용 과 평가용 분할 하기
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3, random_state=156)
# 1. 훈련용독립변수 , 테스트용독립변수 , 훈련용종속변수 , 테스트용종속변수=train_test_split (독립변수, 종속변수 ,test_size=분할비율 , random_state= 난수생성시드)
#test_size=0.3 #훈련용 70%, 테스트용 30% 분할
# print(x_train.shape)
# print(y_train.shape)

#선형 회귀 분석 모델 생성
from sklearn.linear_model import  LinearRegression #분석 모델 객체
from sklearn.metrics import  mean_squared_error, r2_score

#선형 회귀 분석 : 모델 생성
lr=LinearRegression()
# print(lr)
# 4. 모델 훈련
lr.fit(x_train, y_train)
# print(lr.fit)
# print(lr.inercept_) #y절편
#print(Y_predict) #회귀계수
#5. 테스트용으로 예측 하기 # 테스트용에 있는 주택 정보를 이용한 주택 가격 예측 하기
Y_predict=lr.predict(x_test)
# print(Y_predict)

#6. 평가지표 확인하기 (MSE, RMSE, 결정계수 , Y절편, 회귀계수)
mse=mean_squared_error(y_test, Y_predict) #mse 평가
rmse=np.sqrt(mse)
r2=r2_score(y_test, Y_predict)

# print(f'mse:{mse}, rmse:{rmse}, r2:{r2}')
#mse:17.296915907902093, rmse:4.158956107955708, r2:0.757226332313893 1로 가까울 수록 예측을 잘한 것.

print(f'y절편:{lr.intercept_}, 회귀계수:{np.round(lr.coef_,1)}') #np.round(값, 자릿수) : 해당 자릿수에서 반올림 함수


#==========================[3] 결과 시각화===================================#
import  matplotlib.pyplot as plt
import seaborn as sns #산점도 그래프와 선형 회귀 그래프를 함께 그려줌
sns.regplot(x='CRIM',y='PRICE',data=boston_df)
#그래프의 기울기 : 회귀 계수
plt.show() #차트열기
    #y절편 : 독립변수가 0일 때 종속변수의 값
    #-회귀계수 : 독립변수 1증가 할 때 마다 종속변수의 증감 단위 # 기울기
    # -신뢰구간: 좁으면 예측이 안정적이고  관계가 명확하다 해석, 넓다면 예측이 불안정하고 관계가 불명확 하다. - 해석


fig,axs=plt.subplots(figsize=(16,16),ncols=3,nrows=5) #3칸 5줄로 이뤄짐
x_features=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']

for i, feature in enumerate(x_features):    #for 요소 인덱스 , 요소값 in enumerate(리스트):
    print(i)
    print(feature)
    row=int(i/3) #몫 i가 3일 때 몫이 1이 되기 때문에 아랫줄로 내려간다. 그렇게 3줄을 만듦.
    col=i%3 #나머지
    sns.regplot(x=feature,y='PRICE',data=boston_df,ax=axs[row][col]) #ax=axs[row][col] : 차트를 표현할 좌표
plt.show() 