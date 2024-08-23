#app.py

from flask import Flask     #(1) Flask 모듈 가져오기
app=Flask(__name__)
from flask_cors import CORS #(3) CORS 모듈 가져오기
CORS(app)   #(4) 모든 HTTP 경로의 CORS 허용
#(5) 매핑
from controller import *
#(6) Flask 실행

if __name__ == "__main__":
    app.run(debug=True)