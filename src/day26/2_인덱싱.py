#2_인덱싱.py

import tensorflow as tf
'''
-인덱싱
    -원소가 저장된 순서 번호
    -0 번 시작
    
-슬라이싱
    -[시작 : 끝 (미만)]
    
'''
#1. 벡터
vec=tf.constant([10,20,30,40,50])
print(vec)
print(vec[0])
print(vec[0].numpy())
print(vec[-1])
print(vec[0:3])
#2. 행렬
mat=tf.constant([[10,20,30],[40,50,60]])
print(mat[0,2])
print(mat[0,:]) #[행(슬라이싱), 열(슬라이싱) ] #첫번째 행, 전체 열 [:]
print(mat[:,1]) #전체 행[:] #두번째 열 #tf.Tensor([20 50], shape=(2,), dtype=int32)
print(mat[:,:])

#3. 3차원 텐서
tensor=tf.constant( #행렬 2개, 백터 2개 , 열(스칼라)3개
    [ #축1 : 고차원텐서
        [ #축2 : 행렬(1차원 리스트)
            [ #축3 : 벡터(1차원 리스트)
                10,20,30],
            [40,50,60]
         ]
        ,
         [[-10,-20,-30],[-40,-50,-60]]

    ]
)
print(tensor)
print(tensor[0,:,:])
# print(tensor[:,:2,:2])

#연습
#1. 벡터
vector=tf.constant([10,20,30,40,50])
#첫번쨰 스칼라(요소)
print(vector[0]) #tf.Tensor(10, shape=(), dtype=int32)
#문제1] 뒤에서부터 2번째 스칼라(요소) 출력하기
print(vector[-2]) #tf.Tensor([40 50], shape=(2,), dtype=int32)
#문제3] 앞에서 3개 요소 슬라이싱
print(vector[0:3])
#문제3] 뒤에서 4개 요소 슬라이싱
print(vector[-4:])

#2. 행렬
matrix=tf.constant([[1,2,3],[4,5,6],[7,8,9]])
#문제 1 첫번째 행, 두번째 열 요소 인덱싱
print(matrix[0,1])
#문제 2 세번째 행, 첫번째 열 요소 인덱싱
print(matrix[2,0])
#문제 3 첫번쨰 행 전체 슬라이싱
# print(matrix[0:-2])
print(matrix[0,:])
#문제 4 두번째 열 전체 슬라이싱
print(matrix[:,1])
#3. 3차원텐서
tensor=tf.constant([ [[1,2],[3,4]], [[5,6],[7,8]] ])
print(tensor[0,0,0]) #문제1] 가장 첫번쨰 요소 인덱싱, 예]1
print(tensor[-1,-1,-1]) #문제2] 가장 마지막 요소 인덱싱
print(tensor[0,:,:]) #문제3] 첫번째 행렬 슬라이싱,
print(tensor[1,0,:]) #문제4] 두번째 행렬 첫번째 행 슬라이싱