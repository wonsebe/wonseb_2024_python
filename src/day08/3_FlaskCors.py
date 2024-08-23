#FlaskCors.py

'''
    CORS : 교차 출처 자원 공유
    - Cross- origin Resource Sharing
    - 현재 주소에서 다른 주소로부터 통신 요청 하고 현재 주소를 응답 받기


    HTTP
        (유재석) 안녕---요청----> (유재석)
                        <-----응답-----
    CORS 통신 제한
        (유재석) 안녕---요청--->  (강호동)
                    <-----응답--

            :5000 ---------------> :5000
            8080 <---------------- :8080

    CORS 허용
        (1) 방법1: from flask 에 커서를 두고 빨간 느낌표 클릭 후 ->install
            방법2: 상단메뉴->파일->설정->왼쪽메뉴[프로젝트] 하위[인터프리터]
                ->[+] alt+insert-> Flask 검색 후 패키지 선택 -> [패키지 설치]
                -pip: 파이썬에서 패키지 소프트웨어를 설치/관리하는 시스템 (vs) 그레이들

        (2) 모듈 가져오기
            from flask_cors import CORS

        (3) CORS 허용
        CORS (app)


'''
from flask import Flask
app=Flask(__name__)
from flask_cors import CORS
CORS(app)   #모든 경로에 대해 CORS 허용

@app.route('/')
def index():
    return "Hello Python Flask CORS"

if __name__ == "__main__" :
    app.run()