#3_할리스커패매장.py


#1.모듈
from bs4 import  BeautifulSoup
import urllib.request
import pandas as pd

# result=[]   #할리스 매장 리스트를 여러개 저장하는 리스트 변수 , 2차원 리스트
# for page in range(1,51):    #1~50까지 반복
#     #할리스 매장 정보 url
#     url=f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
#     response=urllib.request.urlopen(url)
#     htmlData=response.read()
#     soup=BeautifulSoup(htmlData,"html.parser")
#     # print(soup)
#     tbody=soup.select_one('tbody')
#     # print(tbody)
#     for row in tbody.select('tr'):
#         print(row)
#         tds= row.select('td')
#         store_sido=tds[0].string; print(store_sido)
#         store_name=tds[1].string; print(store_name)
#         store_address=tds[3].string;print(store_address)
#         store_phone=tds[5].string; print(store_phone)
#         store=[store_name,store_sido,store_address,store_phone]
#         result.append(store)    #리스트 안에 리스트 요소 추가 : 2차원 리스트 # [ [] ,[] ,[] ,[] ]
# print(result)


#[code 1]
def hollys_store(result):
    for page in range(1, 51):  # 1~50까지 반복
        # 할리스 매장 정보 url
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
        response = urllib.request.urlopen(url)
        htmlData = response.read()
        soup = BeautifulSoup(htmlData, "html.parser")
        tbody = soup.select_one('tbody')
        for row in tbody.select('tr'):
            if len(row)<=3: break
            tds = row.select('td')
            store_sido = tds[0].string;
            # print(store_sido)
            store_name = tds[1].string;
            # print(store_name)
            store_address = tds[3].string;
            # print(store_address)
            store_phone = tds[5].string;
            # print(store_phone)
            store = [store_name, store_sido, store_address, store_phone]
            result.append(store)  # 리스트 안에 리스트 요소 추가 : 2차원 리스트 # [ [] ,[] ,[] ,[] ]




#[code 0]
def main():
    result = []  # 할리스 매장 리스트를 여러개 저장하는 리스트 변수 , 2차원 리스트
    print(">>할리스 매장 크롤링 중>>>>>>")
    hollys_store(result)
    print(result)
    #py 2차원 리스트 객체를 DataFrame 객체로 변환
    tdl=pd.DataFrame(result,columns=('store','sido-go','address','phone'))
    #DataFrame 객체를 csv 파일로 생성
    tdl.to_csv('hollys.csv', encoding='utf-8',mode='w',index=True)
if __name__=="__main__":
    main()



