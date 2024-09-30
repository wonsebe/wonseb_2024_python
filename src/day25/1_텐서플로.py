#1_텐서플로.py
import numpy as np
#텐서플로 : 텐서(다차원 데이터)를 플로(흐름)에 따라 연산하는 과정을 제공하는 라이브러리
#[1] 모듈 호출
import  tensorflow as tf
#[2]
print(tf)
print(tf.executing_eagerly())
#[3] 텐서플로 연산
a=1
b=1
c=tf.math.add(a,b)
print(c)
print(tf.math) #수학 관련 모듈
print(type(c))
#[4] 텐서 객체에서 결과값을 추출 #.numpy()
print(c.numpy()) #텐서 객체에서 결과값을 추출 #3

#[5]텐서(상수: 스칼라) #tf.Tensor(값, shape=(배열크기), 타입= )
    #1.스칼라 정의
a=tf.constant(1)
b=tf.constant(2)
print(a)  #tf.Tensor(1, shape=(), dtype=int32)
print(b)  #tf.Tensor(2, shape=(), dtype=int32)
    #2. 랭크확인
print(tf.rank(a))
    #3. 스칼라 데이터 타입변환 #.cast(스칼라객체, tf.타입)
a=tf.cast(a,tf.float32) #a스칼라객체의 값을 실수로 변환
b=tf.cast(b,tf.float32)
print(a)
print(b)
    #4. 수학적 함수 #.math
        #(1) 덧셈
c=tf.math.add(a,b)
print(c);
print(tf.rank(c)) #rank는 없음 , 배열없음
        #(2) 뺼셈
print(tf.math.subtract(a,b))
        #(3) 곱셈
print(tf.math.multiply(a,b))
        #(4) 나누기
print(tf.math.divide(a,b))
        #(5) 몫
print(tf.math.floormod(a,b))
print(a+b) #tf.Tensor(3.0, shape=(), dtype=float32) 파이썬 연산과 같음 . 그럼 그냥 이거 쓰지..

#[6] 텐서 (1차원 리스트 : 벡터 ) :#tf.Tensor(,shape=(원소개수,),dtype= )
import  numpy as np
vec1=tf.constant( [10,20,30 ], dtype=tf.float32) #파이썬 리스트
vec2=tf.constant( np.array([10,20,30]),dtype=tf.float32)
print(vec1)
print(vec2)

print(tf.rank(vec1)) #1
print(tf.rank(vec2)) #1
#백터 연산
print(vec1+vec2)
print([10,20,30] + [10,20,30]) #리스트 연결이됨 (더하기 안됨)
print(vec1-vec2)  #빼기
print(vec1*vec2) #곱하기
print(vec1/vec2) #나누기
print(vec1%vec2) #나머지
print(vec1//vec2) #몫
print(vec1 ** 2) # 거듭제곱
print(vec1 ** 0.5) #제곱근
#백터내 요소 총합계
print(tf.reduce_sum(vec1))
print(vec1 +1) #브로드캐스팅 #

#[6] 텐서객체(2차원리스트,: 행렬)
mat1=tf.constant( [[10,20], [30,40]]) #전체를 감싼 대괄호내 원소개수: 행개수/백터개수 #내부 대괄호내 원소개수 : 열개수/스칼라개수
print(mat1) #행과 열인 축이 2개라서 랭크/차수 : 2
'''
tf.Tensor(
[[10 20]
 [30 40]], shape=(2, 2), dtype=int32)
'''
#랭크확인
print(tf.rank(mat1))
# mat2=tf.stack(벡터,벡터)
mat2=tf.stack([[1,0],[-1,2]]) #1차원 리스트2개를 2차원 으로 변환
print(mat2)
print(tf.rank(mat2))

#행렬연산
print(tf.math.multiply(mat1,mat2))
print(mat1 * mat2)
print(mat1 -mat2) #subtract(mat1,mat2)
print(mat1 +mat2) #add(mat1,mat2)
print(mat1 / mat2) #divide(mat1,mat2)
#====================error======================
# print(mat1 % mat2) #오류
# print(tf.math.mod(mat1,mat2)) #나머지 구하는 식
# print(mat1 // mat2) #0을 넣으면 안된다 / 분모가 0이기 때문
#===============================================
print(tf.math.multiply(mat1,3)) #브로드캐스팅

#행(가로) 열(세로) 곱(곱셈) 연산
print(tf.matmul(mat1,mat2))
'''
tf.Tensor(
[[-10  40]
 [-10  80]], shape=(2, 2), dtype=int32)

'''







'''
빅데이터: 많은 자료들                    
머신러닝: 자료들의 학습 모델             (사이킥런)
딥러닝 : 복잡한 자료들의 학습 모델        (텐서플로 라이브러리)
텐서플로 자료구조                           

스칼라     백터      매트릭                         텐서
rank-0  rank-1    rank-2                      rank-3
값       리스트     2차원리스트                  3차원리스트
차수-0    차수-1     차수-2                       차수-3
x       한방향:x    두방향:가로(x)세로(y)    세방향: 가로(x),세로(y),높이(z)

'''





