#controller.py

from app import app     #Flask 객체 호출
from service import personData
@app.route('/', methods =['GET'])
def index() :
    data=personData()   #서비스 처리 후 결과 받기
    #파이썬 객체로는 JSON 에 전송이 불가능.
    #파이썬 객체를 딕셔너리 로 변경 , 객체명.__dict__
    # newData=[]
    # for o in data:
    #     dic= o.__dict__
    #     newData.append(dic)
    # return  newData
    #방법2]
    #위에 코드 4줄 -> 1줄 : map
    data=list(map(lambda o:o.__dict__,data))
    return data
