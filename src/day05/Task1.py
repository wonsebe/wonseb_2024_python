#Task1.py
#문자열 활용 , p.58 ~ p.76
#[조건1]: 각 함수들을 구현해서 프로그램 완성
#[조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#         2. 저장된 여러명의 이름을 모두 출력
#         3. 수정할 이름과 새로운 이름을 입력받아 수정
#         4. 삭제할 이름을 입력받아 존재하면 삭제
names= "유재석, 강호동, 신동엽" #여러개 name들을 저장하는 문자열 변수
#[조건3] : names 변수 외 추가적인 전역 변수 생성 불가능합니다.
#[조건4] : 최대한 리스트타입 사용하지 말기

#하나의 변수에 여러가지 정보 #1.JSON(몇 가지 필드를 Key  로 구분,  2. CSV(몇 가지 필드를 쉼표(,)로 구분 , 주로 문자열 타입
def nameCreate() :
    nameInput= input("이름을 입력해주세요 : ")
    names=nameInput
    print("입력한 이름", names, "(이)가 저장되었습니다.")
    print(names)

def nameRead() :
    for name in names.split(','):
        print(names)    #문자열내 , 쉼표기준으로 분해
    return

def nameUpdate() :
    updateInput=input("수정하려는 이름을 입력해주세요: ")
    newupdateInput=input("새로운 이름을 입력해주세요")
    print(names.replace(updateInput, newupdateInput))
    return

def nameDelete() :
    deleteInput= input("삭제하려는 이름을 입력해주세요")
    names.replace(deleteInput, '')
    print("이름 문자열 내역:", names)
    return


while True: #무한루프
    ch= input("1. create 2. read 3. update 4.delete: ")
    if ch == '1':
        nameCreate()
    elif ch == '2':
        nameRead()
    elif ch == '3':
        nameUpdate()
    elif ch == '4':
        nameDelete()