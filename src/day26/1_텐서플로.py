#1_텐서플로.py

'''
-텐서플로
    1. 구글이 개발한 오픈소스 딥러닝 프레임워크 이다.
    2. 머신러닝, 딥러닝 모델을 만들고 훈련하는데 사용된다
    3. 특히 신경망을 기반으로 한 모델을 구축하고 학습 시키는데 사용된다
    4. 케라스라는 고수준 API 를 제공하고 보다 간단한 모델을 정의하고 훈련할 수 있다.
    5. 그 외 이미지처리 , 자연어 처리 , 음성 인식 등의 다양한 곳에서 활용 된다,
[텐서]
    1. 텐서플로 에서 다루는 기본 데이터 구조이다.
    2. 다차원 배열/리스트 생각할 수 있고 여러 차원으로 표현할 수는 있다.
    3. 텐서(데이터구조)플로(흐름) : 데이터를 처리하고 학습 시키는 과정을 나타낸다.
    4. 종류
        1. 스칼라 # 0차원 텐서 #상수 #0랭크 #0차수 #방향 없음
            -단일 숫자 #5
        2. 벡터 #1차원 텐서 # 1차원 리스트 #1랭크 #1차수 #한 방향 # X 또는 Y #행 또는 열
            -#[5,10,15]
        3. 행렬 #2차원 텐서 #2차원 리스트 #2랭크 #2차수 # 두 방향 #X와 Y #(행,열)
            -행 과 열 로 이루어짐 #[ [5,10],[15,20] ]

        4. 고차원 텐서
            -3차원 텐서 #3차원 리스트 #3랭크 # 3차수 # 세 방향 #X,Y,Z # (높이 , 행 , 열)
            -4차원 텐서 # 4차원 리스트 #4랭크 # 4차수 # 네 방향 #X,Y,Z ,W #(축1,축2,축3,축4)


'''
import tensorflow as tf #텐서플로 모듈 호출
#[1] 스칼라
a=tf.constant(5) #스칼라 정의 #
print(a)#tf.Tensor(5, shape=(), dtype=int32)
print(tf.rank(a))#tf.Tensor(0, shape=(), dtype=int32)
print(a.numpy()) #5 #numpy 값을 뺴옴
print(tf.rank(a).numpy()) #0

#[2] 벡터
a=tf.constant([5,10,15])
print(a) #tf.Tensor([ 5 10 15], shape=(3,), dtype=int32)
print(tf.rank(a)) #tf.Tensor(1, shape=(), dtype=int32)
print(a.numpy())#[ 5 10 15]
print(tf.rank(a).numpy()) #1
#[3] 행렬
a=tf.constant([[5,10],[15,20]])
print(a)
print(tf.rank(a))
#tf.Tensor(
# [[ 5 10]
#  [15 20]], shape=(2, 2), dtype=int32)
print(a.numpy())
#tf.Tensor(2, shape=(), dtype=int32)
# [[ 5 10]
#  [15 20]]
print(tf.rank(a).numpy()) #2

#[4]고차원텐서
# 3차원 텐서 만들기
mat1=[[1,2,3,4],[5,6,7,8]] #2차원 리스트
mat2=[ [9,10,11,12],[13,14,15,16]] #행 2개 열 4개
mat3=[ [17,18,19,20],[21,22,23,24]] # (2,4)
#2. 같은 축 방향으로 2차원 텐서를 나열하기 =>3차원 텐서
tensor1=tf.constant([mat1,mat2,mat3]) #3개의 리스트를 하나의 리스트로 감싼다.
print(tensor1)
print(tf.rank(tensor1))
tensor2=tf.stack([mat1,mat2,mat3]) #stack(): 쌓다 #2차원 리스트 3개를 쌓다.

#4. 벡터로 3차원 만들기
vec1=[1,2,3,4]
vec2=[5,6,7,8]
vec3=[9,10,11,12]
vec4=[13,14,15,16]
vec5=[17,18,19,20]
vec6=[21,22,23,24]

#3차원 텐서 만들기 #벡터(6개), 행렬(3개) 고차텐서(1)
tensor3=tf.constant([[vec1,vec2],[vec3,vec4],[vec5,vec6]])
print(tensor3)
print(tf.rank(tensor3))

#7. 4차원 텐서 만들기
tensor4=tf.stack([tensor1,tensor2])
print(tensor4)
print(tf.rank(tensor4))


'''
arr1=[] 
arr2=[]
arr3=[]
arr4=[]
#행렬
arr5=[arr1,arr2]
arr6=[arr3,arr4]
#고차원 텐서 
tensor= [arr5,arr6]

'''




