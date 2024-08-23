#1.플라스크.py

'''
    Flask
        -파이썬으로 만들어진 웹 프레임워크 ( vs JACA spring )
        -Flask vs 장고
    -설치
        (1)flask 모듈 설치
            방법1: from flask 에 커서를 두고 빨간 느낌표 클릭 후 ->install
            방법2: 상단메뉴->파일->설정->왼쪽메뉴[프로젝트] 하위[인터프리터]
                ->[+] alt+insert-> Flask 검색 후 패키지 선택 -> [패키지 설치]
                -pip: 파이썬에서 패키지 소프트웨어를 설치/관리하는 시스템 (vs) 그레이들

        (2) Flask 모듈 가져오기
            from flask import Flask
        (3) Flask 객체 생성

        (4)Flask 프레임워크 실행
    -HTTP 매핑


'''
#Flask 모듈 가져오기
from flask import  Flask

#Flask 객체 생성
app = Flask(__name__)
#HTTP GET 매핑 설정
@app.route('/')
def index():
    return 'Hello Flask'
#Flask 웹 실행
if __name__ == '__main__':
    app.run(debug=True)

#콘솔확인
#Flask port 확인 : http://127.0.0.1:5000
#테스트: (1) 크롬 웹주소에 http://127.0.0.1:5000 (2) talend api 로 되는지 (3) JS-AJAX