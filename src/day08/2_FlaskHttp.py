#FlaskHttp.py
from flask import Flask #(1)
app=Flask(__name__) #(2)

class Test:
    pass

# ===================HTTP 매핑=================== #
# @app.route('HTTP경로정의
#return : Flask에서 HTTP Response Content-Type : 파이썬의 리스트 타입, 딕셔너리 타입, 문자열 타입(JSON) 제공
@app.route('/', methods=['GET']) #@GetMapping('HTTP경로정의')
def index1():
    return "Hello method GET"
@app.route('/', methods=['POST'])  #@PostMapping()
def index2():
    return [3,3]
@app.route('/', methods=['PUT'])  #@PutMapping()
def index3():
    return {'result' : True}    #spring @ResponseBody와 유사.
@app.route('/', methods=['DELETE']) #@DeleteMapping()
def index4():
    #return Test()   #return Test() #타입오류 , flask에서 파이썬 객체로 HTTP 응답이 불가능하다.
    return "true"
# ============================================== #
if __name__ =="__main__":   #(3)
    app.run(debug=True)     #debug=True 디버그[정보또는 콘솔출력 제공] 모드
