#Task4.py

names=[{'name':'유재석'}, {'name':'강호동'},{'name':'신동엽'}]    #샘플데이터를 넣고 테스트 하는것이 중요.
#함수 정의 , def 함수명(매개변수, 매개변수 ):
def nameCreate():
    global names
    newName = input('newName : ')
    dic = {'name': newName}  # 딕셔너리 구성
    names.append(dic)  # 딕셔너리를 리스트에 삽입
    return

    return
def nameRead():     #순서 1번 : 코드 작성순서
    global names
    for dic in names:  # 리스트내 딕셔너리 하나씩 호출
        print(f'name : {dic['name']}')
    return

def nameUpdate():
    global names
    oldName=input("수정하려는 이름")
    for dic in names:
        if dic['name']==oldName:
            newName=input('수정할 이름:')
            dic['name']=newName #해당 딕셔너리의 속성 값 수정하기
    return

def nameDelete():
    global names
    deleteName = input('deleteName : ')
    for dic in names:
        if dic['name'] == deleteName:  # 만약에 삭제할 이름과 같으면
            names.remove(dic)  # 리스트변수명.remove( 삭제할딕셔너리 )
            return  # 1개만 삭제하기 위해서는 삭제후 return

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