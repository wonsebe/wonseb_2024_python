#1_for문.py


#- while 문과 비슷한 반복문
# - for 문은 한눈에 들어온다는 장점

#(1) for문의 기본 구조

"""
for 변수 in 리스트( 또는 튜플 또는 문자열 ) :
    실행문;
"""

#예제
test_list=['one','two','three']
#'test_list' 이라는 변수가 ['one','two','three'] 를 참조한다.
# JS : let test_list=['one','two','three']
for i in test_list:
    #: 콜론 다음의 실행문 작성시 들여쓰기 주의 , { } 없다.
    print(i)


"""
(JS 방식)
let test_list=['one','two','three']
test_list.forEach(i -> {
    console.log(i);
})
"""

#예제2
#[요소1,요소2,요소3] : 리스트 타입( 여러 요소를 저장 , 요소 수정/삭제 가능)
#[(요소1,요소2),(요소3,요소4),(요소5,요소6)]: 튜플타입, (여러 요소를 저장, 요소 수정/삭제 불가능) - 고정형

a=[(1,2),(3,4),(5,6)]
for (first, last)in a:
    #리스트내 튜플을 하나씩 (요소1,요소2) 튜플 타입으로 반환해서 반복처리 한다.
    #print(first,last)
    print(first+last)

#for문의 이용
#예제3
marks = [90,25,67,45,80]
number=0 #학생 번호
for mark in marks:
    # 들여쓰기 주의
    number =number+1 #학생번호 1증가
    if mark >= 60:  # 만약에 i번째 요소의 값이 60 점 이상이면
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f'{number}번 학생은 불합격입니다.')
        # 파이썬의 if 조건문에는  ( ) 가 없다.
#예제4
# (2) continue : 가장 가까운 for문의 처음으로 돌아가게 되는 키워드
marks = [90,25,67,45,80]
number=0 #학생 번호
for mark in marks:
    number = number + 1
    if mark < 60:
        continue        #가장 가까운 for문으로 이동 , continue 를 만나게 되면 아래 코드는 실행되지 않는다.
    print(f'{number}번 학생 축하합니다. 합격입니다')


#(3) range() : 숫자 리스트를 생성하여 반환해주는 함수
    #range(숫자) : 0부터 숫자 미만 까지 포함하는 range 객체를 만들어준다.
    #range(시작숫자, 끝숫자) : 시작숫자 부터 끝 숫자 미만 까지 포함하는 range 객체를 만들어준다.
    #range(시작숫자, 끝숫자, 증감단위) : 시작숫자 부터 끝숫자 미만까지 증감단위 만큼 증감하여 포함하는 range 객체를 만들어준다.
a = range(10)
print(a)    #1,2,3,4,5,6,7,8,9
a=range(1,11) # 1부터 11
print(a)    #1,2,3,4,5,6,7,8,9,10

#예제
for value in range(10):
    print(value , end=' ') #print(    ,  end =' ') : 줄바꿈 처리를 하지 않는 출력문

print() #예제 구분

for value in range (1,11) : #1~10
    print(value , end=' ')

print() #예제구분

for value in range(1,11,2): #1~10 , 2씩 증가, 1,3,5,7,9
    print(value, end=' ')
print() #예제구분

#예제2 1부터 10까지 누적합계를 구하시오.
sum = 0
for i in range(1,11) :
    sum = sum+i
print(sum)

sum=0
for i in range(1,101): #1~100
    sum= sum+i
print(sum)

#예제4 (구구단)
#1. 단출력 :2~9
for i in range(1,10):       #단
    for j in range(1,10):   #곱
        #print(i*j, end=' ') #출력
    # print('') #줄 띄우기 (단마다)
    # print(' ')
        print(f'{i}X{j} = {i*j:>2} ' , end=' ')
    print(' ')

#(4) 리스트 컴프리헨션 사용
a =[1,2,3,4]
result= [num*3 for num in a]
# [] 안에서 for문을 사용한다.
#[ for 반복변수 in 리스트명 ]
print(result)

#2.
result= [i for i in a]
#반복되고 있는 i 값을 하나씩 리스트 요소로 대입하여 리스트 생성한다.
print(result)

#3. 기존 리스트를 반복문을 활용하여 새로운 리스트 생성
print( [i for i in a] ) #java/js: 리스트명.map( )

#4. 리스트 컴프리헨션 사용,
    #[표현식 for 항목 in 반복가능객체 if 조건문]
    #[연산식 for 반복변수 in 리스트 if 조건문]
    # 2개 이상
        #[
#       표현식 for 항목 in 반복가능객체 if 조건문
#       표현식 for 항목 in 반복가능객체 if 조건문
#                                           ]
result = [num for num in a if num%2 ==0]
print(result)

#5. 2개 이상 ,구구단 예시
result= [ x*y for x in range(2,10)
          for y in range(1,10)]
print(result)











