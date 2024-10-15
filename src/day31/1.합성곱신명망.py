#1.합성곱신경망.py

'''
-딥러닝 프로세스(절차)
    1. 데이터 수집
    2. 데이터 전처리 : 수집된 데이터를 신경망 모델에 적합하게 수정
    3. 데이터 분할 :훈련용 데이터와 검증/데이터 용으로 나눈다. 주로 7:3 cs 8:2
    4. 모델 설계(구축)
        1.Sequential API(클래스) , Functional API(클래스)
        2.레이어 구성 : 입력층 ---> 은닉층(con2D, MaxPooling2D,Flatten)등등 --->은닉층 ---> 출력층 구성
        3.활성화 함수 : 각 레이어 에서 학습된 값을 비선형으로 변환할때 사용. 주로 Relu, softmax 함수 사용

    5. 모델 컴파일 : 모델을 어떻게 학습 하고 평가 하는지 설정
        1. 옵티마이저 : 모델의 가중치를 업데이트하는 방법 , adam: 학습을 기반으로 최적화 알고리즘, sgd: 확률적 경사 하강법
        2. 손실함수 : 실제값과 예측과의 차이 ,분류모델 : sparse_categorical_crossentropy , 회귀 : mean_squared_error
        3. 평가지도: 모델의 성능을 평가하는 지표, 분류모델 : accuracy, 회귀 : mse
    6. 모델 학습
        1. 에포크: 전체 훈련 데이터를 한 번 사용되는 수
        2. 검증 : vaildation_data
    7. 모델 평가
    1. evaluation() : 최종 성능의 손실함수와 평가지표 결과를 볼 수 있다.
----> 모델 튜닝 (하이퍼 파라미터)
    -학습률, 배치 크기, 레이어 수 , 뉴런(노드 수 ) 활성화 함수 , 에포크 등등 여러 하이퍼파라미터 조정하기.
        1. evaluation() : 최종 성능의 손실함수와 평가지표 결과를 볼 수 있다.
    8. 모델 예측
    -predict() :
'''


#1.데이터셋 준비
import tensorflow as tf
import numpy as np

#mnist 손글씨 이미지 데이터 로드
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_vaild,y_valid)=mnist.load_data()

print(x_train.shape,y_train.shape,x_vaild.shape,y_valid.shape)

#새로운 출력 값 배열 생성(홀수:1, 짝수:0)
y_train_odd=[]
for y in y_train:
    if y % 2 ==0:
        y_train_odd.append(0)
    else:
        y_train_odd.append(1)

y_train_odd= np.array(y_train_odd)#넘파이 배열
print(y_train_odd.shape)

print(y_train[:10])
print(y_train_odd[:10])

y_valid_odd=[]
for y in y_valid:
    if y %2 ==0:
        y_valid_odd.append(0)
    else:
        y_valid_odd.append(1)
y_valid_odd= np.array(y_valid_odd) #넘파이 배열
print(y_valid_odd.shape)

#채널 추가, 마지막인덱스(-1) 새로운 축 추가
x_train=x_train/255.0
x_vaild=x_vaild/255.0

x_train_in=tf.expand_dims(x_train,-1)
x_vaild_in=tf.expand_dims(x_vaild,-1)

print(x_train_in.shape,x_vaild_in.shape)

# Functional API 사용해 모델 생성
######################### 합성곱 입력 구조 ############################
#(1) 입력레이어 #파이썬 문법 객체
inputs=tf.keras.layers.Input(shape=(28,28,1))
#(2) 합성곱 레이어 #파이썬 문법 객체
conv=tf.keras.layers.Conv2D(32,(3,3),activation='relu')(inputs)
# conv(inputs) #합성곱 레이어 앞에 입력레이어 연결하기 #입력레이어 <---- 합성곱 레이어 #이렇게 해도됨.

#(3) 폴링 레이어 #파이썬 문법 객체
pool=tf.keras.layers.MaxPooling2D((2,2))(conv)
# pool(conv) #폴링 레이어 앞에 합성곱레이어 연결하기 #__call__ #입력레이어<----합성곱레이어 <--폴링레이어
#(4) 플래톤 레이어 #파이썬 문법 객체
flat=tf.keras.layers.Flatten()(pool)
# flat(pool) #플래톤 레이어 앞에 폴링 레이어 연결 하기 #입력레이어<----합성곱레이어<--폴링레이어 <--플래톤 레이어

######################### 단순 입력 구조 추가 ############################
flat_inputs=tf.keras.layers.Flatten()(inputs) #입력레이어 <--플래톤 레이어
# flat_inputs(inputs)

#################### 2개 입력 구조를 1개 출력으로 만들기 #합치기 ####################
concat=tf.keras.layers.Concatenate()([flat,flat_inputs])
# concat=[flat,flat_inputs] #2개의 입력 구조를 합치기
# 입력레이어 -->합성곱 레이어 --> 폴링 레이어 --> 플래톤 레이어
#--------------------------------------------------------  > Concatnate() 입력레이어합치기 ---> Dense() 출력 레이어
#(5) 출력 레이어
outputs=tf.keras.layers.Dense(10,activation='softmax')(concat)
#(6) 모델
model=tf.keras.models.Model(inputs=inputs,outputs=outputs)

print(model.summary())

#모델 컴파일
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#모델 훈련
history=model.fit(x_train_in,y_train,validation_data=(x_vaild_in,y_valid),epochs=3)

#모델 성능
val_loss,val_acc=model.evaluate(x_vaild_in,y_valid)
print(val_loss,val_acc)

#다중 출력 분류 모델 (1. 다중분류[0~9] 2. 이진분류[0,1] )
    #[1] 입력 1
inputs=tf.keras.layers.Input(shape=(28,28,1),name='inputs')

conv=tf.keras.layers.Conv2D(32,(3,3),activation='relu',name='conv2d_layer')(inputs)
pool=tf.keras.layers.MaxPooling2D((2,2),name='maxpool_layer')(conv)
flat=tf.keras.layers.Flatten(name='flatten_layer')(pool)
    #[2] 입력 2
flat_inputs=tf.keras.layers.Flatten()(inputs)
    #[3] 입력 3
concat=tf.keras.layers.Concatenate()([flat,flat_inputs])
    #[4] 출력레이어 2개
digit_outputs=tf.keras.layers.Dense(10,activation='softmax',name='digit_dense')(concat) #다중분류는 softmax를 쓴다.
odd_outputs=tf.keras.layers.Dense(1,activation='sigmoid',name='odd_dense')(flat_inputs) #이중분류를 할 때는 sigmoid를 사용한다.
    #[5] 모델 생성
model=tf.keras.models.Model(inputs=inputs,outputs=[digit_outputs,odd_outputs])
model.summary()

#모델의 입력과 출력을 나타내는 텐서
print(model.input)
print(model.output)

#모델 컴파일 #다중 출력의 손실함수는 loss={} ,# loss_weights :손실함수의 가중치 1이 100%임.
model.compile(optimizer='adam',loss={'digit_dense':'sparse_categorical_crossentropy','odd_dense':'binary_crossentropy'},
              loss_weights={'digit_dense':1,'odd_dense':0.5},
              #0~9 예측을 더 중요시하게 가중치를 설정했다. #0~9 예측/결과는 100%반영하고 , 홀짝예측/결과는 50% 반영 설정
              #손실계산에 사용할 비중(가중치)
              metrics=['accuracy','accuracy']) #다중 출력에 따른 평가지표를 다중 설정

#모델 훈련 #다중 출력시 훈련용과 검증용이 다중이 되므로 {} 딕셔너리 구조 사용.
history= model.fit({'inputs':x_train_in},{'digit_dense':y_train, 'odd_dense':y_train_odd},
                  validation_data=({'inputs':x_vaild_in},{'digit_dense':y_valid, 'odd_dense':y_valid_odd}),epochs=3)

#모델 성능 평가
model.evaluate({'inputs':x_vaild_in},{'digit_dense':y_valid, 'odd_dense':y_valid,'odd_dense':y_valid_odd})


# #샘플 이미지 출력
# import matplotlib.pylab as plt
# def plot_image(data,idx):
#     plt.figure(figsize=(5,5))
#     plt.imshow(data[idx])
#     plt.axis("off")
#     plt.show()
#
# plot_image(x_vaild,0)

#모델 예측
print(y_valid[0])
digit_preds,odd_preds=model.predict(x_vaild_in)
print(digit_preds[0])
print(odd_preds[0])


# 어제꺼 이어서 기존 코드에 새로운 코드넣어서 새로운 모델 만들기
#전이 학습

#레이어의 name 속성을 이용한 특정 레이어 추출 #앞의 모델에서 flatten_layer 출력을 추출
#(1) 기존의 Functional API 로 생성한 모델에서 특정 레이어 추출해서 새로운 Functional API 모델 생성하기
base_model_output=model.get_layer('flatten_layer').output #특정 레이어와 연결된 레이어까지 추출 - conv <- pooling <- flatten

#앞의 출력을 출력으로 하는 모델 정의
base_model=tf.keras.models.Model(inputs=model.input,outputs=base_model_output,name='base')
print(base_model.summary()) #기존 모델에서 입력층과 출력층은 플래톤까지 레이어

#(2) 출력 레이어 추가하는 새로운 Sequential API 모델 생성하기.
digit_model=tf.keras.Sequential([base_model,tf.keras.layers.Dense(10,activation='softmax')]) #다중 분류여서 softmax를 사용
print(digit_model.summary())

# functional API ( input -> conv -> pooling -> flatten ) -> Dense
#(3) 모델 컴파일
digit_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#(4)
digit_model.fit(x_train_in,y_train,validation_data=(x_vaild_in,y_valid),epochs=3)

#특정 레이어 모델을 속성을 이용해서 훈련이 업데이트 되지 않도록 고정시키자.
#베이스 모델의 가중치 고정
base_model_frozen=tf.keras.models.Model(inputs=model.input,outputs=base_model_output,name='base_frozen')
base_model_frozen.trainable=False # 모델의 파라미터 값이 고정되면서 훈련을 통해서 업데이트 되지 않는다. 훈련이 안됨.
print(base_model_frozen.summary())

#1. Functional API 적용
dense_output=tf.keras.layers.Dense(10,activation='softmax')(base_model_frozen.output)
digit_model_frozen=tf.keras.models.Model(inputs=base_model_frozen.input,outputs=dense_output)
print(digit_model_frozen.summary())

#모델 컴파일
digit_model_frozen.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#모델 훈련
history=digit_model_frozen.fit(x_train_in,y_train,validation_data=(x_vaild_in,y_valid),epochs=3)

#베이스 모델의 Con2D 레이어의 가중치만 고정 (Freeze Layer)
base_model_frozen2=tf.keras.models.Model(inputs=model.input,outputs=base_model_output,name='base_frozen2')
base_model_frozen2.get_layer('conv2d_layer').trainable=False #특정 레이어 name 속성을 이용한 레이어의 파라미터 값을 고정하고 훈련을 취소한다.
print(base_model_frozen2.summary())

#Functional API 적용
dense_output2=tf.keras.layers.Dense(10,activation='softmax')(base_model_frozen2.output)
digit_model_frozen2=tf.keras.models.Model(inputs=base_model_frozen2.input,outputs=dense_output2)
print(digit_model_frozen2.summary())

#모델 컴파일
digit_model_frozen2.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#모델 훈련
history=digit_model_frozen2.fit(x_train_in,y_train,validation_data=(x_vaild_in,y_valid),epochs=3)
