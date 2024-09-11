#2_자동차연비.py

import  numpy as np
import  pandas as pd
data_df=pd.read_csv('./10장_data/auto-map.csv',header=0,engine='python')
# print('데이터셋 크기: ',data_df.shape)
data_df.head()
# print(data_df)
data_df=data_df.drop(['car_name','origin','horsepower'],axis=1, inplace=False)
data_df.head()
# print(data_df)
# print('데이터셋 크기: ',data_df.shape)

data_df.info()
# print(data_df)

#분석 모델 구축 , 결과 시각화
from sklearn.linear_model import  LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#X,Y 분할
Y=data_df['mpg']
X=data_df.drop(['mpg'],axis=1, inplace=False)
#훈련용 데이터와 평가용 데이터 분할하기
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3, random_state=0)
#선형 회귀 분석 : 모델 생성
lr=LinearRegression()
lr.fit(X_train,Y_train)

#선형 회귀 분석() : 평가 데이터에 대한 예측 수행 , 예측 결과 Y_predict 구하기
Y_predict=lr.predict(X_test)

mse=mean_squared_error(Y_test, Y_predict)
rmse=np.sqrt(mse)
print('mse:{0:.3f},RMSE:{0:.3f}'.format(mse,rmse))
print('R^2(Variance score):{0:.3f}'.format(r2_score(Y_test, Y_predict)))

print('Y절편값:', np.round(lr.intercept_,2))
print('회귀계수값:',np.round(lr.coef_,2))

coef=pd.Series(data=np.round(lr.coef_,2), index=X.columns)
coef.sort_values(ascending=False)
# print(coef)

#산점도 시각화 하기
import matplotlib.pyplot as plt
import seaborn as sns
fig,axs=plt.subplots(figsize=(16,16),ncols=3, nrows=2)
x_features=['model_year','acceleration','displacement','weight','cylinders']
plot_color=['r','b','y','g','r']
for i, feature in enumerate(x_features):
    row=int(i/3)
    # print(row)
    col=i%3
    # print(col)
    sns.regplot(x=feature, y='mpg', data=data_df, ax=axs[row][col], color=plot_color[i])
plt.show()
print("연비를 예측하고 싶은 차의 정보를 입력해주세요")
cyliners_1=int(input("cyliners: "))
displacement_1=float(input("displacement: "))
weight_1=float(input("weight: "))
acceleration_1=float(input("acceleration: "))
model_year_1=int(input("model_year: "))
mpg_predict=lr.predict([[cyliners_1, displacement_1, weight_1,acceleration_1, model_year_1]])
print("이 자동차의 예상 연비(MPG)는 %.2f입니다." %mpg_predict)