#1_셀레니움.py

#1. 모듈 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
#[1] 정적 크롤링
def CoffeBean_store(result):
    #2. webdriver 객체 생성
    wd=webdriver.Chrome()

    #3.webdriver 객체를 이용한 웹페이지 접속, get(URL)
    # wd.get("http://www.hanbit.co.kr")
    for i in range(1,10):
        #실습: 커피빈 매장 정보(동적페이지=JS이벤트) 크롤링
        #1. 커피빈 웹페이지 연결
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(2) #1초동안 일시정지(대시상태) #웹페이지가 열릴때까지 2초 기다리기 #컴퓨터 사양에 따라 다를 수 있다.
        #2. 커피빈 웹페이지의 자바스크립트 함수 호출 , .execute_script("JS함수호출)
        try:
            wd.execute_script(f"storePop2({i})")  #31번 매장인 ' 삼성봉은사거리점 ' 모달 창 열린다.
            time.sleep(2)   #스크립트가 실행이 끝날때까지 2초대기 # 컴퓨터 사양에 따라 다를 수 있다.
            #3. 자바 스크립트 함수가 수행된 페이지의 소스 코드를 저장
            html=wd.page_source
            #4. BeautifulSoup 객체 생성
            soupCB1=BeautifulSoup(html,'html.parser')
            #5. HTML 소스 코드 확인
            # print(soupCB1.prettify())

            #6. 특정 매장 정보의 모달창에서 매장 정보 파싱하기
            #매장 지점명
            store_name_h2=soupCB1.select('div.store_txt > h2')
            # print(store_name_h2)#
            store_name=store_name_h2[0].string
            # print(store_name)
            store_info=soupCB1.select('div.store_txt > table.store_table>tbody>tr>td')
            # print(store_info)
            #매장 주소
            store_address_list= list(store_info[2])
            # print(store_address_list)
            store_address=store_address_list[0]
            # print(store_address)
            #매장 전화번호
            store_phone=store_info[3].string
            # print(store_phone)
            #매장정보의 리스트 선언
            store=[store_name,store_address,store_phone]
            #매장 정보 리스트를 매장리스트에 담기, 2차원 리스트
            result.append(store)
        except Exception as e: print(e)
    #for end
    return  result
def main():
    result=[]
    CoffeBean_store(result)
    print(result)
    #판다스를 이용한 2차원 리스트를 데이터프레임 객체로 생성
    CB_tbl=pd.DataFrame(result,columns=['store','address','phone'])
    #데이터프레임 객체 정보를 csv 파일로 변환 저장
    CB_tbl.to_csv('coffeBean.csv',encoding='utf-8',mode='w',index=True)


if __name__=="__main__":
    main()





