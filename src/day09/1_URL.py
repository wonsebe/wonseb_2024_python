#1_URL.py
import urllib.request

#urllib: URL 작업을 위한 여러 모듈을 모은 패키지
    #1. urllib.request.Request(URL): 지정한 URL에 대한 요청 객체를 반환
    #2. urllib.request.urlopen(요청객체): 지정한 요청 객체를 실행하고 응답 객체를 반환
    #2-1 응답객체.getcode(): 응답상태반환(2xx: 성공, 4xx:실패, 5xx:실패)
    #2-2 응답객체.read(): 응답 내용 모두 읽어오기 #.decode('utf-8'):HTML 형식과 한글 형식 지원

#[1] urllib.request: URL 요청에 관련 기능을 제공하는 라이브러리
import urllib.request           #1.request 모듈 호출
요청할주소="https://www.example.com"   #2. 요청을 보낼 url 주소를 가지는 변수
요청객체=urllib.request.Request(요청할주소)     #3.Request 객체 생성 #지정한 URL에 대한 요청을 생성
응답객체= urllib.request.urlopen(요청객체)    #4. urlopen 메소드를 이용한 url 에 대한 요청을 실행하고 응답 객체를 반환함수
print(응답객체)  #<http.client.HTTPResponse object at 0x00000245EA45BA60>
print(응답객체.getcode())   #200
# print(응답객체.read())#b'<!doctype html>\n<html>\n<head>\n ...
print(응답객체.read().decode('utf-8')) #안나옴 위에 read를 했기때문에 하나 주석처리 해야함.


