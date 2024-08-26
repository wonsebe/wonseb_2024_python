#3_tourApi.py
import json
import urllib.request

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

#[code 3]   # 지정한 날짜와 지정한 국가, 구분을 받아서 url 요청 하기
def getTourismStateItem(yyyymm, nat_cd, ed_cd):
    #1. 출입국관광통계의 기본 URL
    base="http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    #2. 매개변수 : 인증키 , 연월 , 국가코드, 출입국구분코드
    parameters=f'?_type=json&serviceKey={인증키}'
    parameters+=f'&YM={yyyymm}&NAT_CD={nat_cd}&ED_CD={ed_cd}'
    url=base+parameters #3. 합치기
    print(f'url:{url}')

    #url 요청후 응답객체 받기
    responseDecode=getRequestUrl(url)   #url요청후 응답객체 받기
    if responseDecode==None : return  None  #5. 만약에 응답객체가 None이면 None 반환
    else: return json.loads(responseDecode) #6. 만약에 응답객체가 존재하면 json형식을 파이썬객체로 변환하는 함수
        # json.loads() JSON 형식--> PY 형식 , json.dumps() PY형식 ---> JSON 형식(문자열 타입) 반환 함수

#[code 4]
def getTourismStateService(nat_cd, ed_cd,nStartYear,nEndYear):
    jsonResult=[]   #수집한 데이터를 저장할 리스트 객체
    dataEND=f'{str(nEndYear)}{str(12)}'#마지막 연도의 마지막 월
    isDataEnd=0 #데이터의 끝 확인하는 변수

    for year in range(nStartYear,nEndYear+1 ):#시작한 연도부터 마지막 연도까지 반복 #range(부터, 미만)
        print(f'>>year :{year} ')
        for month in range(1,13):    #1부터 12월까지 반복
            print(f'>>month: {month}')
            if isDataEnd ==1 :
                break  #만약에 isDataEnd가 1이면 반복문 종료
            #:> : 오른쪽 정렬 > ,2 자릿수, 0빈칸이면 0 채움
            yyyymm=f'{str(year)}{str(month):0>2}'
            print(yyyymm)

            jsonData= getTourismStateItem(yyyymm , nat_cd, ed_cd)
            if jsonData != None :
                print(jsonData)
                #만약에 지정한 날짜의 내용물이 없으면
                if jsonData['response']['body']['items']=='':
                    isDataEnd =1 #지정한 날짜에 내용물이 없으므로 반복문 종료
                    print('>> 데이터 없음')
                    break
                #아니고 내용물이 있으면
                natName= jsonData['response']['body']['items']['item']['natKorNm']#국가명
                natName=natName.replace(' ','')
                num=jsonData['response']['body']['items']['item']['num']#관광객수
                #딕셔너리 : 국가명 , 국가코드 , 연도월, 방문자수
                dic={'nat_name':natName, ' nat_cd':nat_cd, 'yyyymm':yyyymm, 'visit_cnt':num}
                jsonResult.append(dic)  #딕셔너리를 리스트에 담기
                print(natName)
                print(num)
                print(dic)
    #모든 반복문 종료후
    return  jsonResult
#[code 1]
def main():

    # 서비스 요청을 필요한 매개변수들을 입력받기
    nat_cd=int(input("국가코드(중국:112/ 일본:130/ 미국:275): "))#2. 국가코드
    nStartYear=int(input('시작연도 :')) #3.데이터 수집 시작 연도
    nEndYear=int(input('끝연도: '))    #4. 마지막 데이터의 연도
    ed_cd='E' #5. 구분(E: 방한외래관광객, D: 해외 출국 )

    jsonResult=[]
    jsonResult = getTourismStateService(nat_cd, ed_cd,nStartYear, nEndYear)#6. 서비스 요청후 응답 객체 받기
    print(jsonResult)

    #7. 응답받은 py 객체를 json 으로 반환 후 파일처리
    with open(f'{nat_cd}{nStartYear}{nEndYear}.json', "w", encoding="utf-8") as file:
        jsonFile=json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        file.write(jsonFile)

if __name__=="__main__":
    main()

