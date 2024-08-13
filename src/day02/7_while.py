# 7_while.py

# - 문장을 반복해서 수행해야 할 경우

# (1) while 문의 기본 구조

'''
1. 자바
while(조건문) {
        실행문;
        증감식;
}

2.파이썬
초기값;
while 조건문 :
      실행문;
'''

treeHit =0 #변수
while treeHit <10: #변수가 10미만이면 반복하고 아니면 반복종료 한다는 뜻
    #python은 증감식이 없다.
    treeHit = treeHit+1
    print(f'나무를 {treeHit}번 찍었습니다.') #f포메팅: f'문자열{ 코드 }문자열'
    if treeHit==10 :
        print('나무 넘어갑니다.')

        #while , if 주의할 점 : { } 없고 들여쓰기를 이용한 실행문을 제어문에 포함


# (2) while 문 만들기
number =0           #변수
while number != 4:  #변수가 4가 아니면 반복하고 4이면 반복 종료 하겠다는 뜻
    print("1.Add 2.Del 3. List 4. Quit")
    number=int(input())
    #input() : 콘솔창에서 입력받은 값을 반혼해주는 함수
    #int() : 자료를 정수 타입으로 반환 해주는 함수
#while , if  에서는 들여쓰기 주의


#(3) break 키워드 : 가장 가까운 반복문 강제 종료 vs return 함수 종료
coffee=10 #변수
while True: #무한 루프, java: while(true){} , 파이썬에서는 True,False 첫글자를 대문자  # : 콜론 나올때 마다 들여쓰기
   money =int(input('돈을 넣어 주세요'))   #input('입력전 출력문구') : 콘솔에 입력된 값을 반환 함수
   # int(자료 ) : 해당 자료를 정수 타입 반환 함수 , vs JAVA : Integer.parseInt() vs JS : parseInt()
   if money == 300 : #만약에 입력받은 값이 300이면
       print('커피를 줍니다')
       coffee = coffee-1
   elif money>300 : #아니면 , vs  JAVA /JS : else if
       print(f'거스름돈 { money -300}을 주고 커피를 줍니다')
       coffee = coffee-1
   else:
       print(f'돈을 다시 돌려 주고 커피를 주지 않습니다')
       print(f'남은 커피의 양은 { coffee }개 입니다.')


   if coffee ==0 : #만약에 커피가 0개 이면
        print(f'커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break # 가장 가까운 반복문을 강제로 종료한다.

# (4) continue 키워드: 가장 가까운 반복문으로 강제 이동
a=0
while a <10 :
    a +=1       #a의 값이 짝수이면
    if a % 2 ==0 : #a의 값이 짝수 이면
        continue #while문으로 이동한다, 아래 코드는 실행되지 않는다
    print(a)    #짝수는 출력되지 않고, 홀수만 출력된다. 13579

# (5) 무한 루프 ; 조건이 항상 True 이므로 while 안에 있는 실행문은 수행하게 된다. 주로 break 이용한 종료 조건을 만든다.






