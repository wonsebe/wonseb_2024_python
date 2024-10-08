#1_심층신경망.py

import tensorflow as tf

#케라스의 내장된 데이터셋에서 mnist(손글씨 이미지) 데이터셋 로드
mnist=tf.keras.datasets.mnist
print(mnist)

#데이터셋을 다운로드 해서 (훈련용, 테슽트용)
(x_train,y_train),(x_test,y_test)=mnist.load_data()
print(x_train.shape,y_train.shape) #(60000, 28, 28) (60000,)
print(x_test.shape,y_test.shape) #(10000, 28, 28) (10000,)
                                #데이터 크기 , 세로픽셀, 가로픽셀
                                #하나의 이미지는 28*28 픽셀된 이미지.
#시각화
import matplotlib.pyplot as plt
fig, axes= plt.subplots(3,5) # 3행 5열 여러개 차트 표현
fig.set_size_inches(8,5) #전체 차트의 크기를 가로 8인치 세로 5인치

for i in range(15): #0~14 까지 반복문 실행
    ax=axes[i//5, i%5] #i%5 : 몫(행 인덱스) #i%5:나머지(열 인덱스)
    ax.imshow(x_train[i]) #x_train[i] : i번째 이미지
    ax.axis('off') #x,y 축 없애기
    ax.set_title(y_train[i]) # 각이미지(차트)/정답 을 제목으로 출력


plt.show()

#데이터 전처리    #[0:첫번쨰 이미지, 10:15 : 특정한 픽셀, :전체 픽셀
print(x_train[0, :,:]) #5 손글씨 출력

# 0~255 사이가 아닌 0~1 사이를 가질 수 있도록 범위를 정규화하기
print(x_train.min()) #min() : 최소값 찾기 함수 #max() : 최대값잡기 함수
# 데잍터 정규화
x_train=x_train/x_train.max()
print(x_train.min(),x_train.max()) # 0.0 1.0
x_test= x_test / x_test.max()  #테스트용 정규화
print(x_train[0,:,:]) #5손글씨 정규화 후 출력

#Dense 레이어 에는 1차원 배열만 들어갈 수 있으므로 2차원 배열은 1차열 배열로 변경
print(x_train.shape) #(60000, 28, 28)
#방법1] 텐서플로 방법
print(x_train.reshape(60000,-1).shape) #(10000, 28, 28) (10000,) 1차원 -데이터수 , 가로
#방법2] 플레톤 레이어 방법
print(tf.keras.layers.Flatten()(x_train).shape)

#방법1] 레이어 에 활성화 함수 적용할때 #relu 함수
tf.keras.layers.Dense(128, activation="relu")
#128개의 노드, relu 활성화 함수를 적요하는 레이어
#방법2]
model=tf.keras.Sequential( [
    tf.keras.layers.Dense(128), #128개의 노드의 레이어 1개
    tf.keras.layers.Activation("relu")#별도로 활성화 함수 레이어 추가

]) #입력층 명시된 상태 아니고, 1개만 레이어 정의될때는 출력층
#출력층이 128개의 노드로 구성된 모델

#모델 생성
model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),#입력층 #독립변수 784개
        #2차원(이미지) 를 1차원 변환 : Flatten 패턴
        #28*28=784 를 가지는 1차원 배열
    tf.keras.layers.Dense(256,activation='relu'),#은닉층ㅡ
    tf.keras.layers.Dense(64,activation='relu'),#은닉층
    tf.keras.layers.Dense(32,activation='relu'),#은닉층
        #각 레이어들 간의 연결된 완전연결층 이다.
        #각 256, 64, 32 개의 노드를 가지는 은닉층 3개
        #각 relu는 비선형성 활성화 함수 적용

    tf.keras.layers.Dense(10, activation='softmax')#출력층 #종속변수 10개 #분류 모델
        #정답은 0~9 사이의 손글씨 정답 # 0 또는 1또는 2또는 3또는 ~~~~~~9
])
#각 레이어(은닉층)계수, 각 노드의 개수는 중요한 하이퍼 파라미터가 된다.


print(model.summary())
'''
Model: "sequential_1"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten_1 (Flatten)             │ (None, 784)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 256)            │       200,960 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_3 (Dense)                 │ (None, 64)             │        16,448 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_4 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_5 (Dense)                 │ (None, 10)             │           330 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 219,818 (858.66 KB)
 Trainable params: 219,818 (858.66 KB)
 Non-trainable params: 0 (0.00 B)
None
'''

#이진분류 ; 출력 노드가 1개, sigmoid 일경우
model.compile(loss='binary_crossentropy')
# (2) y가 원핫 백터 인경우
    #y=5 일떄 원핫 =[ 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 ]
model.compile(loss='categorical_crossentropy')
# (2) y가 원핫 백터가 아닐 때
    #y=5
model.compile(loss='sparse_categorical_crossentropy')

#[3-7] 옵티마이저

#(1)클래스로 지정하는 방법
# adam=tf.keras.optimizers.Adam(lr=0.001)
adam=tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=adam)

#(2) 문자열로 지정하는 방법
model.compile(optimizer='adam')

#[3-8] 평가지표
#(1) 클래스로 지정하는 방법
acc=tf.keras.metrics.SparseCategoricalAccuracy()
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=[acc])
#(2) 문자열로 지정하는 방법
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#[3-9] 훈련 #fit(훈련독립변수 , 훈련종속변수 , epochs= 학습반복수 , validation_data=(테스트독립변수,테스트종속변수)
model.fit(x_train , y_train, epochs=10, validation_data=(x_test,y_test))

#[3-10]평가
test_loss, test_acc=model.evaluate(x_test, y_test)
print(test_acc)#1에 가까울수록 좋은 성능 #백분율

#[3-11] 예측
import numpy as np
predictions=model.predict(x_test)
print(predictions[0])

# 가장 높은 확률만 추출 np.argmax() : 배열내 가장 큰 값을 가진 인덱스 반환 함수
print(np.argmax(predictions[0])) #인덱스 7
#가장 앞에 있는 10개 예측값 확인 #np.argmax(   , axis=차원수 (축) )
print(np.argmax(predictions[:10],axis=1) ) #예측10개 확인: [7 2 1 0 4 1 4 9 5 9]

print(y_test[:10]) #예측값 정답 10개 확인: #[7 2 1 0 4 1 4 9 5 9]

#데이터 시각화
def get_one_result(idx):
    img,y_true,y_pred,confidence=x_test[idx],y_test[idx],np.argmax(predictions[idx]),100*np.max(predictions[idx])

    return img,y_true,y_pred,confidence

#canvas 생성
fig,axes=plt.subplots(3,5)
fig.set_size_inches(12,10)
for i in range(15):
    ax=axes[i//5,i%5]
    img,y_true,y_pred,confidence=get_one_result(i)
    #imshow로 이미지 시각화
    ax.imshow(img,cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f'True{y_true}')
    ax.set_xlabel(f'prediction:{y_pred}\n confidence: ( {confidence:2f} %)')
plt.tight_layout()
plt.show()



















