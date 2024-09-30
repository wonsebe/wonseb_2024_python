#5.자동미분.py



'''
미분 : 미세한 부분
    -실제 y(종속변수) , 예측 y ---> 평균제곱오차 # 딥러닝 : 더 복잡하게 계산

    -일차방정식을 구하는 방법
        기울기 m, 점(지나는점) xy, ab
        1. m=y증가량/x증가량
        2. m=(y-b)/(x-a)
        3. 분모 소분 #  (x-a)*m=(y-b)*/(x-a)*(x-a)
        4. m(x-a)=(y-b)
        5. y=m(x-a)+b
            -기울기 3, 점:(1,2)
            y= 3(x-1)+2
            y=3x-1
            절편: y=-1, x=-3/1
    -일차 방정식 : y= ax+b
        -b(y절편) #y절편 이란 : a가 0일 때 y의 값 #x절편 이란? y축이 0일 때 x축의 값

'''

#p.45

#1. 텐서플로 모듈 호출
import tensorflow as tf
#. 선형 관계를 갖는 데이터 샘플 생성 #y=3x-2
    #1. 텐서플로의 랜덤 숫자 생성 객체 선언 #시드값은 아무거나
g=tf.random.Generator.from_seed(2020 ) #시드란 : 랜덤 생성할 때 사용되는 제어 정수값
    #2. 랜덤숫자 생성 객체를 이용한 정규분포 난수를 10개 생성해서 벡터(리스트) x에 저장한다.
    #.normal(shape=(축1,축2))  .normal(shape=(축1,축2,축3))
x=g.normal(shape=(10,))
y=3*x-2
print(x.numpy()) #독립
print(y.numpy()) #종속

#3. loss 함수 정의 #손실함수 (평균 제곱 오차) 를 정의하는 함수
def cal_msg(x,y,a,b):
    y_pred=a*x+b  #y값 종속(예측) =계수(기울기)a * x(피처) +상수항(y절편)
    squared_error=(y_pred-y) **2 #예측 y 와 실제 y 간의 차이의 제곱 계산(오차제곱)
    mean_squared_error= tf.reduce_mean(squared_error) #모든 오차 제곱의 평균을 계산하여 반환
    print(mean_squared_error)
    return mean_squared_error

#4. 자동 미분 과정을 기록
a=tf.Variable(0.0) #계수 #텐서플로 변수에 0으로 초기화
b= tf.Variable(0.0)#y절편 #텐서플로 변수에 0으로 초기화
# 목적: a 와 b를 미세하게 변경하면서 반복적으로 계산 하여 손실을 최소화 하는 값을 찾는다.
EPOCHS=200 #계산횟수 #에포크
for epoch in range(1,EPOCHS+1): #총 200회 까지
    # 200번 반복하면서 목적 : a와 b를 미세하게 변경하면서 손실/차이 가 가장 적은 값을 찾자.
    #4-1 msg 기록 #tf.GrandientType() as 변수: with 안에 있는 계싼식을 모두 기록하는 역할 #mse 를 tape에 기록한다.
    with tf.GradientTape() as tape:
        mse=cal_msg(x,y,a,b) #위에서 정의한 손실함수를 계산한다.

        #4-2 기울기 계산 #tape.gradient()를 이용하여 mse에 대한 a와b의 미분값(기울기)를 구한다.
        grad=tape.gradient(mse, {'a':a , 'b':b}) #mse에 대한 a와 b를 딕셔너리로 반환한다.
        d_a=grad['a']
        d_b=grad['b']

        # assign_sub() 텐서풀로 변수에 매개변수를 원본값에서 뺀 값으로  변수값을 수정
        a.assign_sub(d_a * 0.05)  # 현재값의 5% 감소
        b.assign_sub(d_b * 0.05)  # 0.05감소

        #중간 계산 확인
        if epoch %20 ==0 : #20번마다 #epoch=반복횟수  #mse: 평균제곱오차 #a계수 #b상수항
            print(f'{epoch},{mse:.4f},{a.numpy():.2f},{b.numpy():.2f}')




