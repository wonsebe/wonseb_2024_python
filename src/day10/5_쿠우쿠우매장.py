#5_쿠우쿠우매장.py
from bs4 import  BeautifulSoup
import urllib.request
import pandas as pd
from flask import  Flask
# 전국 쿠우쿠우 매장 정보(번호,매장명,연락처,주소,영업시간)
# pandas 이용한 csv 파일로 변환
# (3) 플라스크 이용한 쿠우쿠우 전국 매장 정보 반환하는 HTTP 매핑 정의한다.
    #HTTP(GET): 5000/qooqoo
    #(3) 생성된 csv 파일 읽어서 json 형식을 반환
#[code 1]
def qooqoo_store(result):
    for page in range(1, 7):  # 1~6까지 반복
        url=f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        response=urllib.request.urlopen(url)
        htmlData=response.read()
        soup=BeautifulSoup(htmlData,"html.parser")
        tbody=soup.select_one('tbody')
        # stores = soup.find_all(class_='td-num hidden-md hidden-sm')
        # print(stores)
        # print(tbody)
        for row in tbody.select('tr'):

            tds=row.select('td')
            if len(tds) <= 1: continue
            # print(tds)
            store_qno= tds[0].string
            print(store_qno)
            store_name = tds[1]
            print(store_name)
            # store_phone = tds[2].string;
            # # print(store_phone)
            # store_address = tds[3].string;
            # # print(store_address)
            # store_time=tds[4].string;
            # print(store_time)

            # store = [store_qno, store_name, store_phone, store_address, store_time]
            # result.append(store)  # 리스트 안에 리스트 요소 추가 : 2차원 리스트

#[code 0]
def main():
    result=[]
    print(">>쿠우쿠우 매장 크롤링 중")
    qooqoo_store(result)
    print(result)
    # py 2차원 리스트 객체를 DataFrame 객체로 변환
    # tdl = pd.DataFrame(result, columns=('store', 'sido-go', 'address', 'phone'))
    # # DataFrame 객체를 csv 파일로 생성
    # tdl.to_csv('hollys.csv', encoding='utf-8', mode='w', index=True)

if __name__=="__main__":
    main()