#1_합성신경망.py

#텐서플로 라이브러리 불러오기
import tensorflow as tf

#2. 데이터셋 #손글씨
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_vaild,y_vaild)=mnist.load_data()
#x_train : 28*28 픽셀된 0~9 숫자
#y_train : 훈련용 0-9 숫자
#x_vaild : 테스트용 0-9 숫자, 종속변수
print(x_train.shape,y_train.shape)  #(60000, 28, 28) (60000,) #6만개의 28*28 이미지 -3차원(60000,) #1차원
print(x_vaild.shape,y_vaild.shape)  #(10000, 28, 28) (10000,) #만개의 28*28 이미지 -3차원 (10000,) #1차원
print(x_train[0,:,:]) #첫번째 데이터의 손글씨 0~255 #2차원 형식으로 표현
print(y_train[0]) #첫번째 데이터의 손글씨 정답 #5



#시각화
import matplotlib.pylab as plt

def plot_image(data,idx):
    plt.figure(figsize=(5,5))
    plt.imshow(data[idx],cmap="gray") #차트에 이미지 표현 함수 #inshow() #5
    plt.axis("off")
    plt.show()
plot_image(x_train,0)




#4. 정규화 # 각 픽셀 값을 255 로 나누어 0~1 사이의 값으로 변환해 모델 학습을 더 빠르고 안정적이게 만들기
print(x_train.min(), x_train.max(),x_vaild.min(), x_vaild.max()) #정규화 전
x_train=x_train/255.0
x_vaild=x_vaild/255.0
#y(종속변수)는 정규화를 하지 않는다. (정답이니까)
print(x_train.min(), x_train.max(),x_vaild.min(), x_vaild.max()) #정규화 후

#5.채널 축 # 채널이란? 색상정보를 가지는 구성 요소
#흑백(모노컬러) 이미지를 위해 1개 채널 추가
print(x_train.shape,x_vaild.shape) #파이썬에서 배열에 축 추가하는 방법 #(60000, 28, 28) (10000, 28, 28) 3차원
x_train_in=x_train[...,tf.newaxis] #3차원 ---> 4차원
x_vaild_in=x_vaild[...,tf.newaxis]
print(x_train_in.shape,x_vaild_in.shape) #(60000, 28, 28, 1) (10000, 28, 28, 1) 4차원
#가장 앞 차원은 ...을 뒤에 넣어라.

#모델 생성
#model=tf.keras.Sequential([입력레이어,은닉레이어,은닉레이어,출력레이어])
model=tf.keras.Sequential([
    #////////////은닉////////////////////////

    tf.keras.layers.Conv2D(32,(3,3),activation='relu', input_shape=(28,28,1),name='conv'),  #Conv2D(합성곱) #입력레이어
        #32,(3,3) : 32개의 필터를 가진 3*3 크기의 합성곱 레이어 추가
        #relu: Relu 활성화 함수를 사용
        #input_shape=(28*28,1) : 독립변수의 차원 모양 (3차원) , (가로,세로,채널)
    #풀링 레이어
    tf.keras.layers.MaxPooling2D( (2,2) ,name='pool'),

        #2*2 크기의 최대 플링 레이어 추가, 특성맵 크기를 줄인다.
    # 플레톤 레이어
    tf.keras.layers.Flatten(), #다차원 배열을 1차원 배열로 반환

    #////////////은닉///////////////////////
    #출력 레이어
    tf.keras.layers.Dense(10,activation='softmax')
        #종속변수가분류할 데이터가 0-9이므로 10개 #다중분류에서는 주로 softmax함수 사용
])

#7. 모델 컴파일 #옵티마이저 , 손실함수, 평가지표 설정
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    #옵티마이저 : adam 옵티마이저로 설정
    #손실함수 : 분류모델의 오차 계산법인 엔트로피 설정
    #평가지표 : 분류모델의 정확도 계산법인 accuracy 설정

#모델 훈련
history=model.fit(x_train_in, y_train, # 훈련용 데이터와 훈련용 정답
                  validation_data=(x_vaild_in,y_vaild),  #테스트용 데이터와 테슽트용 정답
                  epochs=10) #전체 데이터셋을 10회 반복하여 훈련한다.
#9.훈련된 손실 , 정확도 확인하기
model.evaluate(x_vaild_in,y_vaild) #테스트용 독립변수와 테스트용 종속변수(정답)을 평가하기

#10. 손실화 정확도 시각화
def plot_loss_acc(history,epoch):
    loss=history.history['loss'] #훈련 손실(오차)값
    val_loss=history.history['val_loss'] #테스트 손실(오차 값)
    acc=history.history['accuracy']#훈련 정확도
    val_acc= history.history['val_accuracy'] #테스트 정확도

    #서브플롯 차트 구성
    fig,axes=plt.subplots(1,2,figsize=(12,4))#1행 2열로 구성된 서브플롯
    axes[0].plot(range(1,epoch+1),loss,label='Training')#x축 훈련수 #y축은 훈련 오차값
    axes[0].plot(range(1, epoch + 1), val_loss, label='Validation')#x축 훈련수 #y축은 테스트 오차 값

    axes[0].legend(loc='best') #x축 훈련수 #y축은 정확도
    axes[0].set_title('Loss') #x축 훈련수 #y축은 테스트 정확도

    axes[1].plot(range(1, epoch + 1), acc, label='Training')
    axes[1].plot(range(1, epoch + 1), val_acc, label='Validation')
    axes[1].legend(loc='best')
    axes[1].set_title('Accuracy')

    plt.show()
plot_loss_acc(history,10)

#11. 훈련된 모델로 예측하기
print(y_vaild[0])#종속변수 #10000개 중에 첫번째 손글씨의 정답
print(tf.argmax(model.predict(x_vaild_in[0]))) #독립변수 #테스트용으로 예측하기. #이미지된 손글씨 #예측한 것의 첫번째인덱스의 최댓값
#argmax(): 배열내 가장 큰 값을 가진 요소의 인덱스 변환


# model.summary()
# print(model.inputs)
# print(model.outputs)
# print(model.layers)
# print(model.layers[0])
# print(model.layers[0].input)
# print(model.layers[0].output)
# print(model.layers[0].weights)
#
# print(model.layers[0].kernel)
#
# print(model.layers[0].bias)
#
# model.get_layer('conv')
#
# activator=tf.keras.Model(inputs=model.inputs,outputs=[layer.output for layer in model.layers[:2]])
# activations=activator.predict(x_train_in[0][tf.newaxis,...])
#
# len(activations)
#
# conv_activation=activations[0]
# conv_activation.shape
# fig,axes=plt.subplots(4,8)
# fig.set_size_inches(10,5)
#
# for i in range(32):
#     axes[i//8 , i%8].matshow(conv_activation[0,:,:,i],cmap='viridis')
#     axes[i // 8, i % 8].set_title('kernel %s'%str(i),fontsize=10)
#     plt.setp(axes[i//8 , i%8].get_xticklabels(),visible=False)
#     plt.setp(axes[i // 8, i % 8].get_yticklabels(), visible=False)
#
# plt.tight_layout()
# plt.show()
#
# pooling_activation=activations[1]
# print(pooling_activation.shape)
#
# fig,axes=plt.subplots(4,8)
# fig.set_size_inches(10,5)
#
# for i in range(32):
#     axes[i // 8, i % 8].matshow(conv_activation[0, :, :, i], cmap='viridis')
#     axes[i // 8, i % 8].set_title('kernel %s' % str(i), fontsize=10)
#     plt.setp(axes[i // 8, i % 8].get_xticklabels(), visible=False)
#     plt.setp(axes[i // 8, i % 8].get_yticklabels(), visible=False)
#
# plt.tight_layout()
# plt.show()
