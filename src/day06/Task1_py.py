# Task1_py
names="유재석,강호동,신동엽"    #샘플데이터를 넣고 테스트 하는것이 중요.

    #하나의 변수에 여러개의 이름을 저장하는 방법
    #변수란? 하나의 자료를 저장하는 메모리 공간
    # 하나의 자료에 여러가지 속성을 담는 방법 : 1. 객체    2. 문자열(JSON 형식< CSV 형식)  3. 리트스  4.튜플  5. 딕셔너리
        #타입(자료분류) vs 형식(자료모양)
        # "10" : 문자열타입 , 정수형식
        # 10 : 정수 타입, 정수형식
        # "{key:value}" : 문자열 타입, json형식
        # {key:value}: json/딕셔너리 타입, json/딕셔너리 형식
#함수 정의 , def 함수명(매개변수, 매개변수 ):
def nameCreate():
    global names
    #함수안에서 전역변수를 호출하는 방법 , global 전역변수명
    newName=input('newName :')  #저장할 새로운 이름 입력하기
    #첫등록이면 가장앞에, (쉼표)가 없어도 된다.
        #삼향연산자 : 참 if 조건문 else 거짓
        #문자열.count(문자):문자열내 문자 개수 반환
    names += f'{''if names.count(',')==0 else ','}{newName}'  #(쉼표) 이름을 구분하는 구분문자(CSV 형식)
    return
def nameRead():     #순서 1번 : 코드 작성순서
    global names
    #for 반복변수 in 리스트명:   #리스트내 요소 하나씩 반복변수에 대입 , js: 리스트명.forEach( 반복변수 =>{} )
    #for 반복변수 in 문자열: #문자열내 문자 하나씩 반복변수에 대입
    #문자열.split( '특정문자' ): #문자열내 특정문자 기준으로 분해해서 리스트로 반환 함수

    for name in names.split(","):
        print(f'name:{name}')   #f'문자열{코드}문자열' #js:`문자열{코드}문자열`
    return
def nameUpdate():
    global names    #전역변수 호출
    #문자열(불변성 특징), #부분수정x  #문자열내 중간에 다른 문자열 변경
    #만약에 동일한 문자열을 찾아서 새로운 문자열로 변경
    oldName = input('oldName :')
    if names.find(oldName) == -1:
        return
    else:
        newName = input('newName:')
        #names = names.replace(oldName, newName)
        newNames=""
        for name in names.split(','):    #이름 하나씩 반복
            if name ==oldName :
                newNames +=f'{''if newNames=="" else ','}{newName}' #새로운 이름
            else:
                newNames +=f'{''if newNames=="" else ','}{name}'    #기존이름
        names=newNames  #새로 구성한 이름명단을 전역변수에 대입
    return
def nameDelete():
    global names    #전역변수 호출
    #만약에 동일한 문자를 찾아서 ''로 변경
    deleteName=input('deleteName :')#문자열.find(문자) #문자열내 찾을문자가 존재하면 인덱스반환 #없으면 -1
    if names.find(deleteName)==-1:
        return
    else : #존재하면
        #문자열.replace(기존문자, 새로운문자) #문자열내 기존문자가 존재하면 새로운문자로 치환해서 반환
        #names=names.replace(f'{deleteName}' , '')
        #replace 이름 단위가 아닌 문자 단위 치환이 되므로 문제 발생 할 수 있다.
        newNames=""
        for name in names.split(','):
            if name == deleteName:
                continue   #가장 가까운 반복문으로 이동
            else:
                newNames += f'{''if newNames=="" else ','}{name}'
            names=newNames
        return


while True: #무한루프 # {} 대신 : 과 들여쓰기를 사용 #true 소문자가 아닌 True 대문자로 작성
    ch= int( input("1. create 2. read 3. update 4.delete: ") )
    #int() 문자열타입 -> 정수타입 반환 함수
    # #input()입력함수 , 입력받은 데이터를 문자열 반환
    #ch: 'ch' 변수에 특정한 타입을 작성하지는 않는다.
    if ch ==1 : #만약에 #조건문
        nameCreate()
        #주의할점 : 들여쓰기
    #들여쓰기 1번 -> while문에 포함
        #들여쓰기 2번 -> while 문 안에 if 문에 포함
    elif ch==2:
        nameRead()

    elif ch==3:
        nameUpdate()

    elif ch==4:
        nameDelete()

