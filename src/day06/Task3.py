#Task3.py
#튜플이란? 리스트와 비슷, 차이점 : 요소의 삽입/삭제가 불가능
    #튜플은 불변성을 가진다.리터럴과 같다.
    # a=3+2          ,  5
    # a='py'+3       , py3
    # a=(1,2) +(3)    , (1,2,3)
names=('유재석','강호동','신동엽')    #샘플데이터를 넣고 테스트 하는것이 중요.
#함수 정의 , def 함수명(매개변수, 매개변수 ):
def nameCreate():
    global names
    newName=input('새로 추가할 이름을 입력해주세요: ')
    names +=(newName ,) #기존 튜플과 입력받은값의 튜플 더하기 해서 새로운 튜플 변환
    return

def nameRead():     #순서 1번 : 코드 작성순서
    global names
    for name in range(len(names)):
        print(names[name])
    # print(names)
    return

def nameUpdate():
    global names
    oldName=input('수정하려는 이름을 입력해주세요:')
    if names.count(oldName)== 0: return
    else:
        newName =input("수정할 이름을 입력해주세요:")
        newNames=()
        for name in names:
            if name == oldName:
                newNames += (newName, )
            else:
                newNames += (name ,)
        newName=newNames
    return

def nameDelete():
    global names
    oldName=input('삭제하려는 이름을 입력해주세요: ')
    if names.count(oldName) ==0 : return
    else:
        newNames =()
        for name in names:
            if name ==oldName:
                continue
            else:
                newNames += (name ,)
            names=newNames      #반복문이 종료되면 새로운 튜플을 전역

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