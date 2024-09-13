#2_유방암진단분석.py


import numpy as np
import pandas as pd

#[1] 데이터 준비하기
from sklearn.datasets import  load_breast_cancer
b_cancer=load_breast_cancer()   #내장된 데이터 호출

#[2] 데이터 탐색하기
# print(b_cancer.DESCR) #내장 데이터의 설명서 호출

#독립변수 : b_cancer.data
# print(b_cancer.data) #독립변수들   #피처
# print(b_cancer.feature_names) #독립변수들의 이름
# print(b_cancer.target) #종속변수 #타겟 # 진단결과  # 1이면 양성, 0이면 음성

b_cancer_df=pd.DataFrame(b_cancer.data,columns=b_cancer.feature_names)
b_cancer_df['diagnosis']=b_cancer.target #종속변수로 정함 : target
b_cancer_df.head()
# print(b_cancer_df.head())

# print("유방암 진단 데이터셋 크기:" , b_cancer_df.shape) #크기 알려줌 369 개의 행,  31개의 열
b_cancer_df.info() #데이터 프레임의 속성 정보 , 용량 ,메모리
# print(b_cancer_df)

# 전처리 과정 을 이용한 특정 값을 표준화한 후에 머신러닝 알고리즘 사용하면 성능을 향상할 수 있다.
'''
-데이터 크기가 크게 다른 경우 모델의 성능이 저하 될 수 있으므로 사용된다.
'''
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
b_cancer_scaled=scaler.fit_transform(b_cancer.data) # 데이터를 표준화하기
# print(b_cancer.data[0]) #표준화 전

'''
[1.799e+01 1.038e+01 1.228e+02 1.001e+03 1.184e-01 2.776e-01 3.001e-01
 1.471e-01 2.419e-01 7.871e-02 1.095e+00 9.053e-01 8.589e+00 1.534e+02
 6.399e-03 4.904e-02 5.373e-02 1.587e-02 3.003e-02 6.193e-03 2.538e+01
 1.733e+01 1.846e+02 2.019e+03 1.622e-01 6.656e-01 7.119e-01 2.654e-01
 4.601e-01 1.189e-01]
'''

# print(b_cancer_scaled[0])# 표준화 후
'''
[ 1.09706398 -2.07333501  1.26993369  0.9843749   1.56846633  3.28351467
  2.65287398  2.53247522  2.21751501  2.25574689  2.48973393 -0.56526506
  2.83303087  2.48757756 -0.21400165  1.31686157  0.72402616  0.66081994
  1.14875667  0.90708308  1.88668963 -1.35929347  2.30360062  2.00123749
  1.30768627  2.61666502  2.10952635  2.29607613  2.75062224  1.93701461]
'''

#[3] 분석 모델링 구축
#독립변수와 종속변수 만들기
X=b_cancer_scaled #독립변수 #스케일링(표준화) 한 데이터 독립변수
Y=b_cancer_df['diagnosis'] #종속변수 만듦

#훈련용 데이터 , 평가용 데이터 분할
from sklearn.model_selection import  train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3, random_state=0)

#모델 객체 생성
from sklearn.linear_model import LogisticRegression
lr_b_cancer=LogisticRegression()

#훈련용 데이터를 피팅(훈련) 하기
lr_b_cancer.fit(X_train,Y_train)
#예측 하기  #평가용으로 수행
Y_predict=lr_b_cancer.predict(X_test)   #이진 예측

# print(Y_predict)

'''#결과
[0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 1 0 1 0 1 0 1
 0 1 0 0 1 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 1 1 0 0 0 1 1 0 1 0 0 0 1 1 0 1 0
 0 1 1 1 1 1 0 0 0 1 0 1 1 1 0 0 1 0 0 0 1 1 0 1 1 1 1 1 1 1 0 1 0 1 1 1 1
 0 0 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 1 1 0 1 1 0 1 0
 1 1 1 1 1 1 1 0 1 0 1 0 0 1 1 0 1 0 0 0 1 1 1]
'''
# print(lr_b_cancer.predict_proba(X_test))

'''
 # 이진 확률 예측
[[9.98656121e-01 1.34387864e-03]
 [3.85539075e-02 9.61446092e-01]
 [1.30479850e-03 9.98695202e-01]
 [1.03486175e-02 9.89651383e-01]
 [2.45036205e-04 9.99754964e-01]
 [5.86881697e-03 9.94131183e-01]]

'''
from sklearn.metrics import confusion_matrix, accuracy_score
#오차 행렬
confusion_matrix(Y_test,Y_predict)
# print(confusion_matrix(Y_test,Y_predict))
# [[ 60   3]
#  [  1 107]]

#2.정확도
from sklearn.metrics import  precision_score , recall_score , f1_score,roc_auc_score
accuracy=accuracy_score(Y_test,Y_predict) #정확도 예측결과 , 실제값을 더한 것 #모델이 전체 데이터에서 얼마나 잘 예측했는지?

#3. 정밀도
precision=precision_score(Y_test,Y_predict)
print(precision)                #0.9727272727272728  #97%이상 #모델이 양성으로 예측한 것 중에서 실제 양성 비율

#4. 재현율
recall=recall_score(Y_test,Y_predict)
print(recall)                   #0.9907407407407407  #97%이상 #실제 양성 중에서 모델이 얼마나 잘 양성으로 예측 했는지?

#5. F1스코어
f1=f1_score(Y_test,Y_predict)
print(f1)                       #0.981651376146789   #97%이상 #정밀도와 재현율의 균형

#6. ROC기반 AUC 스코어
roc_auc=roc_auc_score(Y_test,Y_predict)
print(roc_auc)                  #0.9715608465608465  #97%이상 # 모델이 양성과 음성을 구별하는 능력 평가
    #5. 5가지의 모델 평가 지수 계산 방법 #1. (100%) 에 가까울수록 모델은 예측을 잘 표현하고 있다.

        #대략 85% 이상이면 신뢰도가  높은 편에 속함
#확인
# print('정확도: {0:.3f}, 정밀도:{1:.3f}, 재현율 :{2:.3f}, F1:{3:.3f}'.format(accuracy, precision, recall, f1))
#정확도: 0.977, 정밀도:0.973, 재현율 :0.991, F1:0.982
# print('ROC_AUC: {0:.3f}'.format(roc_auc))  #ROC_AUC: 0.972
