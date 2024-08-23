

#app.py

'''
삼성전자주가.csv 파일의 정보를 테이블 형식으로 localhost:8080/index3.html 출력하시오.
    1. csv 파일을 읽어서 한줄씩 딕셔너리로 변환 후 리스트에 담기
    2.플라스크 이용한 http 매핑 정의하기
    3. 스프링 서버에서 AJAX 를 이용한 플라스크 서버로 부터 삼성전자주가 정보 응답받기
'''

from flask import Flask #(1)Flask 모듈 가져오기
app=Flask(__name__) #(2) Flask 객체 생성
from flask_cors import CORS #(3) CORS 모듈 가져오기 #CORS: 교차 출처 자원 공유 허용
CORS(app)   #(4) 해당 Flask 객체내 모든 HTTP 에 대해 CORS 허용

#(5)매핑
from controller import  *

if __name__=="__main__":
    app.run(debug=True)