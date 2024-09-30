#4.변수.py

import tensorflow as tf
#1. 행렬 텐서
tensor1=tf.constant([ [0,1,2],[3,4,5]])
print(tensor1)

#2. 텐서플로 변수 생성 #tf. Cariable()
tensor_var1=tf.Variable(tensor1)
print(tensor_var1)

#constant() 값 설정 불가능 , Variable()값 설정 가능
#3. 텐서플로 변수 속성 확인
print(tensor_var1.name) #텐서플로 변수명
print(tensor_var1.shape) # 크기 #(2,3)
print(tensor_var1.dtype) # 데이터 자료형/타입
print(tensor_var1.numpy()) #[[0 1 2][3 4 5]]

#4. 텐서플로 변수 데이터 변경/수정/새로운 할당 #자료형 과 크기 동일 해야한다.
tensor_var1.assign([ [1,1,1],[2,2,2] ])
print(tensor_var1)
print(tensor1)

#5. 텐서플로 변수 --> 텐서 변환
tensor2=tf.convert_to_tensor(tensor_var1)
print(tensor_var1) #array([[1, 1, 1],[2, 2, 2]])>
print(tensor2) #tf.Tensor([[1 1 1]  [2 2 2]], shape=(2, 3), dtype=int32)

#6. 텐서플로 변수에 name 속성의 정의
tensor_var2=tf.Variable(tensor2, name='name Name')
print(tensor_var2)

#7. 텐서플로 변수의 연산
print(tensor_var1+tensor_var2)
