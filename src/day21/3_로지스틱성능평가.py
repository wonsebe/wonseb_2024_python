#3_로지스틱성능평가.py

#시험 실제 합격 목록
y_true = [ 0, 0, 0, 1, 1, 0, 1, 1, 1, 1 ] # 시험 실제 합격 목록
y_pred = [ 0, 0, 0, 0, 0, 1, 0, 1, 1, 1 ] # 시험 예측 합격 목록

#[1] 오차정렬함수
from sklearn.metrics import  confusion_matrix
print(confusion_matrix(y_true,y_pred))      #오차 행렬 #confusion_matrix(실제값, 예측값)
# [[3 1]
#  [3 3]]

'''
    오차행렬
    
        -실제 클래스(값)은 행
        -예측 클래스(값)은 열
        - TN    FP
          FN    TP
        -TP(true positive) : 실제 값이 양성(1) 이고 예측도 양성(1) 인 경우    ex] 3
        -TN(true negative) : 실제 값이 음성(0) 이고 예측도 음성(0) 인 경우    ex] 3
        -FP(false positive) : 실제 값이 음성(0) 이고 예측값은 양성(1) 인경우  ex] 1
        -FN(false negative) : 실제 값이 양성(1) 이고 예측값은 음성(0) 인 경우 ex] 3
        
        
    -정밀도 계산식 : 예측값이  POSITIVE 인 데이터 중 인 것 중에 참(TP) 인것의 비율 계산
                    -양성으로 예측한 값들 중에서 실제 양성 비율 
              TP                  3          3
     정밀도= -------            ------  =  -------
             FP+TP               1+3         4
            
    -재현율 계산식: 실제 POSITIVE 데이터를 정확히 예측했는지 평가 #민감도
                        -실제 양성인 값들 중에서 모델이 양성으로 정확하게 예측한 비율
    
                        TP          3             1
        재현율(TPR) = ----------  -------- =    --------
                       FN+TP        3+3           2
                       
                       
    -F1 스코어 : 정밀도와 재현율을 결합한 평가지도 , 정밀도와 재현율이 서로 상충관계인 문제점을 고려하여 정확한 평가
                 #정밀도와 재현율의 조화 평균으로 서로간의 균형을 측정 지표
                         
                             정밀도*재현율                   0.75 *0.5
                         2 X -------------- =        2X -------------------
                              정밀도+재현율                  0.75 + 0.5

    - ROC 기반 AUC 스코어:  실제 nagative 인 데이터를 Postive 로 거짓으로 예측한 비율
                            -FPR이 변할 떄 TPR이 어떻게 변하는지 나타내는 곡선이다    
                  FP             1            1
        FPR =  --------   +  ---------  = ---------
                FP+TN           1+3           4

'''
#[2]정밀도 함수
from sklearn.metrics import  precision_score    #정밀도 알려주는 라이브러리
print(precision_score(y_true,y_pred)) #0.75         #높을수록 정밀하다 해석

#[3] 재현율 함수
from sklearn.metrics import  recall_score
print(recall_score(y_true,y_pred)) #0.5     # 높을 수록 예측이 잘 재현 되고 있다 해석

#[4] f1 스코어 함수
from sklearn.metrics import f1_score
print(f1_score(y_true,y_pred)) #0.6 #높을수록 정밀도와 재현율의 균형이 잘 맞춰져 있다 해석

#[5] ROC 기반의 AUC 스코어 함수 #roc_auc_score
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_true,y_pred)) #0.625      #1에 가까울수록 좋은 성능이다 해석




