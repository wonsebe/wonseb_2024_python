#2_결정트리.py

#어종 데이터셋
#주제: 여러 어종의 특성(weigth,Length,Diagonal,Height,width) 들을 바탕으로 어종명(Species) 예측 하기
#species : 어종명 , weigth: 무게 , length: 길이 , Diagonal: 대각선길이 , height: 높이, width: 너비
#[1]
import  pandas as pd
import numpy as np
data=pd.read_csv('https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv', sep="\s+")
# print(data.head())
# print(data.shape) #(159, 6)
# print(data.info)
#[2] 7:3 비율로 훈련용과 테스트 용으로 분리하기
#인덱스 제거, 독립변수 이름만 리스트에 저장
data_name=data.iloc[:,1].values.tolist()
# print(data_name)
feature_names=['weigth','length','Diagonal','height','width'] # 독립변수 이름
b_df=pd.DataFrame(data, columns=feature_names )
Y=b_df['species'] = target
X=b_df
#훈련용,테스트용 파일 읽어오기
X_train=pd.r
#[3] 결정트리 모델로 훈련용 데이터 피팅 하기

#[4] 훈련된 모델 기반으로 테스트용 예측하고 정확도 확인하기
#출력예시 ]  개선 전 결정트리 모델 정확도 : 0.625
#[5] 최적의 하이퍼 파라미터 찾기 #params ={'max_depth':[2,6,10,14],'min_samples_split:[2,4,6,8] }
# 출력예시] 평균 정확도 : 0.xxxxxxxxx, 최적 하이퍼파라미터:{'max_depth':xx,'min_samples_split:x }
#[6] 최적의 하이퍼 파라미터 기반으로 모델 개선후 테스트용 데이터 예측하고 예측 정확도 확인하기 #시각화하기
#출력예시 ] 개선 후 결정트리모델 정확도: 0.xxx
# 차트 시각화
