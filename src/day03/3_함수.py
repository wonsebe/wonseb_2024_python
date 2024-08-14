#3_함수.py

#입력값을 가지고 어떤 일을 수행한  후 그 결과물을 내어 놓는 것
# 사용목적 : 1. 코드재활용(반복사용) 2. 기능별분리(가독성 좋다)

#(1) 파이썬의 함수의 구조


"""

(1) py
def 함수명( 매개변수 , 매개변수 ) :
    실행문
    return 반환값

(2)
function 함수명( 매개변수 , 매개변수 ){
    실행문
    return 반환값 또는 생략
}

(3) JAVA
반환타입 함수명( 타입 매개변수 ,타입 매개변수 ) {
    실행문 ;
    return 반환값 또는 생략

}

"""
#예1: 함수의 이름은 add 이고 입력으로 2개 (a,b)의 값을 받으면 리턴값(a+b)은 2개의 입력값을 더한값이다.
def add (a,b) :
    # {}가 없으므로 들여쓰기 주의
    return (a+b)
#함수 호출
add(3,4) #add 함수에 3과 4를 매개변수로 전달하여 7을 반환 받았다.
print(add(3,4)) #출력
a=3
b=4
result =add(a,b)        #리터럴 대신 변수를 대입해도 된다.
print(result)           #7


#(2) 입력값과 리턴값에 따른 함수의 형태

#1. 매개변수0 리턴 0
def add(a , b):       # 함수 정의
    result =a+b
    return  result
a=add(3,4)      #함수 호출
print(a)

#2. 매개변수 X 리턴 0
def say():          #함수 정의
    return 'Hi'
a=say()             #함수 호출 시 인수 전달이 없고 반환값을 받아 'a'변수에 저장
print(a)

#3. 매개변수 0 리턴 X
def add(a,b):     # 함수 정의
    print(f'{a},{b}의 합은 {a+b} 입니다')
add(3,4)    #함수 호출 시 인수 2개 전달하여 반환값은 없다.

#4. 매개변수 X 리턴 X
def say():      # 함수 정의
    print('Hi')
#함수 호출 시 인수 없고 반환값도 없다.
say()

#(3) 매개변수를 지정하여 호출하기
def sub(a,b):
    return a- b
print(sub(b=3, a=7))

#함수 호출시 인수의 값를 대입할 매개변수를 지정
result =sub(b=3, a=7)
print(result)
result =sub( a=7, b=3)
print(result)


#(4) 입력값이 몇 개가 될지 모를 때 , 가변 매개변수
#1.
def add_many(*args):
    print(args)     #여러개의 매개변수 값이 들어있는 리스트
    result = 0 #더한 값을 저장하기 위한 변수
    for i in args:  #여러개 매개변수 리스트를 반복처리
        result += i     # 누적합계
    #for 종료후
    return  result  #함수 종료시 반환되는 값

#함수 호출
result =add_many(1,2,3); print(result)
result =add_many(1,2,3,4,5,6,7,8,9,10); print(result)

#2.특정 매개변수를 먼저 작성하고 뒤로 여러개의 매래변수를 작성한다
def add_mul(choice, *args): #여러개의 매개변수와 특정 매개변수가 존재할때는
    print(choice)   #1개의 자료 매개변수
    print(args)     #여러개의 자료를가지는 튜플(매개변수)
    if choice =="add":      #만약에 매개변수값이 add이면
        result =0
        for i in args:
            result = result +i  #누적합계
    elif choice =="mul":        #아니고 만약에 매개변수 값이 mul 이면
        result=1
        for i in args:
            result =result*i      #누적곱
    return  result                #반환값
#함수호출
result= add_mul('add' , 1,2,3,4,5)  #choice ='add' , args = (1,2,3,4,5)
print(result)
result=add_mul('mul',1,2,3,4,5)
print(result)

#(5)키워드 매개변수 .kwargs키워드 , **인수로 전달된 키와값을 딕셔너리의 매개변수로 받는다.
#1.
def print_kwargs(**kwargs):
    print(kwargs)   #{'a': 1} 딕셔너리 타입으로 매개변수를 받는다
                    #{'name': 'foo', 'age': 3}

print_kwargs(a=1)   #인수로 전달시 키와 값으로 전달
print_kwargs(name='foo' , age=3)

#(6)함수의 리턴값은 언제나 하나이다. 여러개 일때는 [] ,{}, () 활용
#1.
def add_and_nul(a,b):
    튜플 = 1 , 2
    print(튜플)
    return a+b , a*b
result=add_and_nul(3,4)
print(result)                   #(7,12) , 튜플1개(튜플안에 요소2개)

#2 동일한 수준의 return 은 하나만 존재해도 된다
def add_and_nul(a,b):
    return a +b
    return a*b # 위에 리턴이 존재하므로 해당 리턴은 실행되지 않는다

#3.서로 다른 수준의 return 은 여러개 존재할 수 있다.
def add_and_nul(a,b):
    if a<0:
        return #만약에 a가 0보다 작으면 함수 강제 종료, 아래 코드는 실행되지 않는다
    return  a+b

#(7) 매개변수에 초깃값 미리 설정하기, 함수 정의할 때 매개변수의 디폴트값 대입하기
    #주의할점: 초기화 하고 싶은 매개변수는 항상 뒤쪽에 놓아야한다.
    #say_myself(name, age, man=True) [0]
    #say_myself(name, man=True, age ) [x]
def say_myself(name, age, man=True):
    print(f'나의 이름은 {name}입니다')
    print(f'나이는 {age}살 입니다')
    if man:
        print('남자입니다')
    else:
        print('여자입니다')
#함수 호출
#만약에 해당 매개변수의 인자값이 없으면 디폴트(초깃)값이 대입된다
say_myself('박응용' , 27)#나의 이름은 박응용입니다 나이는 27살 입니다 남자입니다
say_myself('박응용', 27, False) #나의 이름은 박응용입니다 나이는 27살 입니다 여자입니다

#(8) 함수안에서 선언한 변수의 효력범위 , 지역변수
    #함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다.
a=1         #함수 밖 'a'
def vertest(a):
    a=a+1   #지역변수 'a'; a=2 지역변수의 2는 함수 종료시 사라진다.
vertest(a)
print(a)        #전역변수 'a'의 값 확인 ,1

#함수안에서 함수 밖 변수를 함수안에서 활용하는 방법

#1. return , 권장 한다.
a=1
def vertest(a):
    a=a+1
    return a    #지역변수는 함수 종료시 사라지므로 함수를 호출했던 곳으로 반환
a=vertest(a)
print(a)        # 2

#2. global 키워드: 함수 밖 변수를 함수 안으로 호출할 때 사용하는 키워드
a=1
def vertest():
    global a    #함수 밖에 있는 a변수를 함수 안으로 호출
    a=a+1
print(a)        #2

#3. 지역변수의 특성: 함수 밖에서 함수 안으로 접근 가능하지만 , 함수 안에서 함수 밖으로는 접근이 불가능하다.
b=1
def vertest():
    c=b+1       #함수 밖에 있는 b변수를  함수 안에서 호출, global 없이도 가능.
    return  c
vertest()
print(b)        #2



















































