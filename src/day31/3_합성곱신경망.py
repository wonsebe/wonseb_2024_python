#3_합성곱신경망.py

import  tensorflow as tf
# 1. 데이터셋 로드, 16가지 종류의 의류 이미지 데이터셋
fashion_mnist=tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_valid, y_valid)=fashion_mnist.load_data()

# Functional API 이용한 모델생성(다중 입력)과 예측 테스트
print( x_train.shape )

#채널 추가 , 마지막 인덱스(-1)새로운 축 추가
x_train=x_train/255.0
x_valid=x_valid/255.0

x_train_in=tf.expand_dims(x_train,-1)
x_valid_in=tf.expand_dims(x_valid,-1)

print(x_train_in.shape,x_valid_in.shape)

#functionnal api 사용해 모델 생성
## 합성곱 입력 구조 ##
#(1) 입력 데이터 #파이썬 문법 객체
inputs=tf.keras.layers.Input(shape=(28,28,1))
#(2) 합성곱 레이어
conv=tf.keras.layers.Conv2D(32,(3,3),activation='relu')(inputs)
#(3) 폴링ㅇ 레이어
pool=tf.keras.layers.MaxPooling2D((2,2))(conv)
#(4) 플래톤 레이어
flat=tf.keras.layers.Flatten()(pool)

flat_inputs=tf.keras.layers.Flatten()(inputs)
concat=tf.keras.layers.Concatenate()([flat,flat_inputs])
#출력 레이어
outputs=tf.keras.layers.Dense(10,activation='softmax')(concat)
#(6) 모델
model=tf.keras.Model(inputs=inputs,outputs=outputs)
print(model.summary())

#모델 컴파일
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#모델 훈련
history=model.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=10)

#모델 성능
val_loss,val_acc=model.evaluate(x_valid_in,y_valid)
print(val_loss,val_acc)

############################## 외부 '가방' 이미지의 예측
#1.파이썬 OpenCV : 이미지 파일을 파이썬으로 호출하는 모듈 제공
import cv2
#2. 외부 이미지 가져오기
img=cv2.imread('bag.jpg')
print(img)
print(img.shape)
#3. 이미지 사이즈의 변경
img=cv2.resize(img,dsize=(28,28)) #모델이 학습한 사이즈와 동일하게
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
# 정규화
img=img/255.0

#변경된 이미지 cv시각화
cv2.imshow('img',img)
cv2.waitKey()
result=model.predict(img[ tf.newaxis, ...])
print(result)
print( tf.argmax( result[0]).numpy() )
# img = cv2.imread('')
# img = cv2.resize( img , dsize=( 32 , 32) )
#
# img = img / 255.0
# result = model.predict( img[ tf.newaxis , ... ] )
# print( tf.argmax( result[0]).numpy() )
