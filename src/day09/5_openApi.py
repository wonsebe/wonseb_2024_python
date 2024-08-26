#5. openApi.py


#연습문제 : 서울 열린데이터 광장에서 '민주주의 서울 자유제안'을 클로링하여 JSON 파일로 저장하시오.
인증키 ="nwPZ%2F9Z3sVtcxGNXxOZfOXwnivybRXYmyoIDyvU%2BVDssxywHNMU2tA55Xa8zvHWK0bninVkiuZAA4550BDqIbQ%3D%3D"
#[code 2]
def getRequestUrl(url):
    요청객체=urllib.request.Request(url)
    try:
        응답객체=urllib.request.urlopen(요청객체)
        if 응답객체.getcode() ==200:
            return 응답객체.read().decode('utf-8')
    except Exception as e:
        return None
#[code 3]
def
#[code 1]
def main():
    sn_cd=int(input("조회하고 싶은 제안의 코드 폐의약품:196924 / 플로깅:196923/ 서울시립과학관:196922 :"))
    start_index=int(input("시작번호를 입력하세요:"))
    end_index=int(input("끝 번호를 입력해주세요: "))


    jsonResult=[]
    jsonResult=getProposalSystem(sn_cd,start_index,end_index)
    print(jsonResult)


if __name__=="__main__":
    main()

