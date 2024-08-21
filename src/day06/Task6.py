# day06 > Task6.py
# 객체/리스트 활용 190p. ~ 207p
# [조건1] : 각 함수 들을 구현 해서 프로그램 완성하기
# [조건2] :  1. 한명의 name , age 를 입력받아 저장 합니다.
#           2. 저장된 객체들을 name , age 을 모두 출력 합니다.
#           3. 수정할 이름을 입력받아 존재하면 새로운 name , age 을 입력받고 수정 합니다.
#           4. 삭제할 이름을 입력받아 존재하면 삭제 합니다.
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능합니다.
# 제출 : git에 commit 후 카톡방에 해당 과제가 있는 링크 제출


names = [ ]

class personInfo:
    def __init__(self, name,age):  # 생성자
        self.personname = name
        self.personage= age

def nameCreate( ) :
    global names
    newName=input("이름을 입력해주세요: ")
    newAge=input("나이를 입력해주세요: ")
    names.append(personInfo(newName,newAge))
    return

def nameRead( ):
    global names
    for dic in names:  # 리스트내 딕셔너리 하나씩 호출
        print(f"name = {dic.personname}, age = {dic.personage}")
    return
def nameUpdate(  ) :
    global names
    oldName = input('oldName : ')
    for dic in names:
        if dic.personname == oldName:
            newName = input('newName : ')
            dic.personname = newName  # 해당 딕셔너리의 속성 값 수정 하기.
            newAge = input('newAge : ')
            dic.personage = newAge
            return
    return
def nameDelete( ) :
    global names
    deleteName = input('deleteName : ')
    for dic in names:
        if dic.personname == deleteName:  # 만약에 삭제할 이름과 같으면
            names.remove(dic)  # 리스트변수명.remove( 삭제할딕셔너리 )
            return  # 1개만 삭제하기 위해서는 삭제후 return
    return
while True :
    ch = int( input('1.create 2.read 3.update 4.delete : ') )
    if ch == 1 : nameCreate( )
    elif ch == 2 : nameRead( )
    elif ch == 3 : nameUpdate( )
    elif ch == 4 : nameDelete( )