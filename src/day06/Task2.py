# Task2_py



    #하나의 변수에 여러개의 이름을 저장하는 방법
    #변수란? 하나의 자료를 저장하는 메모리 공간
    # 하나의 자료에 여러가지 속성을 담는 방법 : 1. 객체    2. 문자열(JSON 형식< CSV 형식)  3. 리트스  4.튜플  5. 딕셔너리
        #타입(자료분류) vs 형식(자료모양)
        # "10" : 문자열타입 , 정수형식
        # 10 : 정수 타입, 정수형식
        # "{key:value}" : 문자열 타입, json형식
        # {key:value}: json/딕셔너리 타입, json/딕셔너리 형식
#내가 한 리스트 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
names=['유재석','강호동','신동엽']    #샘플데이터를 넣고 테스트 하는것이 중요.
#함수 정의 , def 함수명(매개변수, 매개변수 ):
def nameCreate():
    global names
    newName=input('새로 추가할 이름을 입력해주세요:')
    names.append(newName)
    return

def nameRead():     #순서 1번 : 코드 작성순서
    global names
    for name in names:  # for 반복변수 in 튜플/리스트/문자열 :
        print(f'name : {name}')
    return

def nameUpdate():
    global names
    oldName = input('수정하고싶은 이름을 입력해주세요 : ')
    # 만약에 수정할 이름이 존재하지 않으면
    if names.count(oldName) == 0:
        return
    else:  # 존재하면 # 수정할 이름의 인덱스 찾기  ,
        # 리스트변수명.index( 찾을값 ) : 리스트내 찾을값이 존재하면 인덱스 반환
        index = names.index(oldName)
        newName = input('수정할 이름을 입력해주세요 : ')  # 새로운 이름
        names[index] = newName  # 찾은 인덱스에 새로운 값 대입
    return

def nameDelete():
    global names
    oldname = input('삭제할 이름을 입력해주세요 :')
    if names.count(oldname)==0 : return
    else:
        names.remove(oldname)
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


#강사님 리스트**********************************************************************

