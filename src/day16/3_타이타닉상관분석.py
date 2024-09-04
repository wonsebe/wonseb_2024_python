#3_타이타닉상관분석.py

#seaborn 라이브러리에 내장된 '타이타닉' 데이터 가져오기
import seaborn as sns #titanic 데이터가 내장되어 있음
titanic= sns.load_dataset('titanic')
print(titanic)

#2. 내장된 데이터를 호출해서 csv 파일로 저장
titanic.to_csv('타이타닉',index=True)

#3. 결측값(누락된값/공백)
print(titanic.isnull().sum())     #결측값 확인
 #4. 결측값을 치환 , fillna()null(결측)값 특정 값으로 채워주는 함수
    #(1) age 열의 결측값을 중앙값(크기순으로 정렬된 상태에서 위치한 값 뜻)으로 치환
    # median(): 중앙값 반환해주는 함수
titanic['age']=titanic['age'].fillna(titanic['age'].median() )
print(titanic.isnull().sum())
    #(2). embarket 열의 결측값을 최빈값(집합의 빈도가 가장 높은 값)으로 치환
print(titanic['embarked'].value_counts())
'''
S    644
C    168
Q     77
'''
titanic['embarked']=titanic['embarked'].fillna('S')
print(titanic.isnull().sum())#확인 embarked에 결측값이 없어짐.
    #(3). embark_town 열의 결측값을 최빈값(집합의 빈도가 가장 높은 값)으로 치환
print(titanic['embark_town'].value_counts())
titanic['embark_town']=titanic['embark_town'].fillna('Southampton')
print(titanic.isnull().sum())#확인 embarked에 결측값이 없어짐.
    #(4). deck 열의 결측값을 최빈값(집합의 빈도가 가장 높은 값)으로 치환
print(titanic['deck'].value_counts())
titanic['deck']=titanic['deck'].fillna('C')
print(titanic.isnull().sum())#확인 deck 결측값이 없어졌다.

titanic.info()#데이터의 기본정보
titanic.survived.value_counts()#survived(생존자여부) 속성의 레코드 개수
#=====================================차트====================================================
#1. 남자 승객과 여자 승객의 생존율
import matplotlib.pyplot as plt
f,ax=plt.subplots(1,2,figsize=(10,5))   # subplots() 서브플롯을 이용한 한번에 여러개 플롯 띄우기
#titanic['survived'][titanic['sex'] =='male'].value_counts() : 성별이 남자인 생존자여부 , explode=[0,0.1]:두번째 조각을  10%정도 떨어뜨림
titanic['survived'][titanic['sex'] =='male'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
#titanic['survived'][titanic['sex'] =='male'].value_counts().plot.pie(explode=[0,0.1],
# autopct='%1.1f%%' : 원형차트 구성   #autopct : 원형차트 백분율 표시 , ax=ax[0] :첫번째 자리
titanic['survived'][titanic['sex'] =='female'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[1],shadow=True)
ax[0].set_title('Survived (Male)')
ax[1].set_title('Servived (Female)')
plt.show()# 남자승객 생존률은 18.9% , 여자 승객은 74.2% 확인

#2.객실 등급별 생존자 수 #x축 : 등급(속성명) , hue=생존자여부(개수)   #등급별 생존자여부 개수  #data=데이터프레임
sns.countplot(x='pclass',hue='survived',data=titanic)
plt.title('Pclass vs Survived')
plt.show() #생존자는 1등급에서 가장 많고 사망자는 3등급이 가장 많다.

    #예) 동행 여부 속성 (alone) 따라 생존자 수
sns.countplot(x='alone', hue='survived', data=titanic)
plt.show() #혼자 왔을 때 사망자가 더 많다






#상관 분석 #연속형 데이터만 가능 #회귀분석과 다른점 : 예측치 없음  동일한 점 : 모두 연속형 쓴다.
    #연속형 데이터만 가능하므로 연속형 데이터 열만 추출  .select_dtypes(include[타입1,타입2):
titanic2=titanic.select_dtypes(include=[int,float,bool])
#연속형 데이터만 존재했을 때 상관분석 실행
titanic_corr=titanic2.corr(method='pearson')    #pearson 얘가 열과 행의 (2차원 테이블 )정보를 보여준다
print(titanic_corr)
#상관계수 :  0~1 정도와 방향을 하나의 수치 요약 # 0관계가 거의 없다 ~ 1관계가 강하다.
    #양의 상관관계는 한 변수가 증가하면 다른 변수도 증가한다.
    #음의 상관관계는 한 변수가 증가하면 다른 변수는 감소한다.
#분석: 남자성인은 생존여부와 음의 상관관계, 객실등급은 생존여부와 음의 상관관계, 혼자탑승한경우 음의 상관관계
    #남자가 증가하면 생존여부 감소한다. 객실등급이 증가하면 생존여부가 감소한다.



#상관계수를 csv에 저장
titanic_corr.to_csv('타이타닉상관계수표.csv',index=True)

#특정한 변수 사이의 상관 계수 추출
            #종속변수                   #독립변수
print(titanic['survived'].corr(titanic['adult_male']))#-0.5570800422053259
            #종속변수                   #독립변수
print(titanic['survived'].corr(titanic['fare'])) #0.2573065223849622

