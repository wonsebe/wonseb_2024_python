#1_클래스.py
'''
    객체란? 논리적/물리적 정의한 실체물
    클래스란? 객체를 물리적으로 표현하기 위한 설계도
    인스턴스란? 클래스를 이용해서 객체를 물리적으로 만든 실체물
'''

#[1]파일썬에서 클래스 만들기
class Calculator:
    def __init__(self): #생성자
        self.result=0
    def __add__(self, num): #메소드
        self.result += num
        return self.result

#[2]파이썬에서 객체 만들기 , 변수명=클래스명()
cal1=Calculator();  print(cal1) #<__main__.Calculator object at 0x000001450EB79520>
cal2=Calculator();  print(cal2) #<__main__.Calculator object at 0x000001450EB79550>

#[3]파이썬 객체내 메소드 호출
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

#[4] 클래스의 생성자 정의
class 과자틀:
    #파이썬은 기본적으로 다중 생성자를 지원하지 않는다.   #단일 생성자 #__init__
#     #기본 생성자
#     def __init__(self):
#         self.과자재료1 = None
#         self.과자재료2 = None

    #생성자1: 매개변수 2개 갖는 생성자
    def __init__(self, 재료1, 재료2): #__init__생성자 역할을 하는 메소드
        #self : 해당 메소드를 실행하는 객체
        self.과자재료1=재료1  #self.필드명=매개변수  #매개변수로 필드 값 초기화 하기
        self.과자재료2=재료2  #self.필드명=매개변수  #매개변수로 필드 값 초기화 하기


#(2)과자 객체 생성
var1= 과자틀('밀가루', '초코'); print(var1)
var2= 과자틀('밀가루','치즈'); print(var2)

#(3) 객체의 필드 호출 , 객체변수명.필드명
print(var1.과자재료1)   #첫번째 과자의 과자재료1 필드값 호출
print(var1.과자재료2)   #첫번째 객체/과자의 과자재료2 필드값 호출
print(var2.과자재료1)   #첫번째 객체/과자의 과자재료2 필드값 호출
print(var2.과자재료2)   #두번째 객체/과자의 과자재료2 필드값 호출
#(4) 객체의 필드값 수정
# var3=과자틀(); print(var3)   #파이썬은 단일 생성자만 가능하다
var2.과자재료2='녹차'
print(var2.과자재료2)   #녹차
