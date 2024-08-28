#service.py

# 1. 모듈 가져오기
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import json

# [1] 잡코리아  정보 크롤링 서비스
def jobkoreaInfo(result):
    for page in range(1, 6): #1~5페이지
        # 2. 지정한 url 를 호출해서 응답 받기
        url=f"https://www.jobkorea.co.kr/Search/?stext=java&tabType=recruit&Page_No={page}"
        response=urllib.request.urlopen(url)
        if response.getcode() ==200:
            print('>>통신성공')
            # 3. 통신 응답 결과를 읽어 와서 크롤링 파싱 준비
            soup=BeautifulSoup(response.read(), "html.parser")
            # 4. 분석한 HTML 식별자들을 파싱 , find , findall , select , select_one
            list=soup.select_one('.list'); #print(list)
            rows=list.select('.list-item '); #print(rows) # 4-1 테이블 전체 파싱
            for row in rows:    # 4-2 테이블(전체매장) 마다 행(매장) 파싱
                # print(row)
                cols = row.select('div');
                # 각 정보들을 파싱 , *공백 제거
                회사명=cols[0].select('a')[0].string.strip(); #print(회사명)
                # print(회사명)
                공고명=cols[1].select_one('.information-title > a').text.strip();
                # print(공고명)
                경력=cols[1].select_one('.chip-information-group').select('li')[0].text.strip();
                # print(경력)
                학력=cols[1].select_one('.chip-information-group').select('li')[1].text.strip();
                # print(학력)
                계약유형=cols[1].select_one('.chip-information-group').select('li')[2].text.strip();
                # print(계약유형)
                지역=cols[1].select_one('.chip-information-group').select('li')[3].text.strip();
                # print(지역)
                count=len(cols[1].select_one('.chip-information-group').select('li'))
                if count >=5:
                    채용기간=cols[1].select_one('.chip-information-group').select('li')[4].text.strip()
                else:
                    채용기간=''
                # print(채용기간)

                #5. 파싱한 정보를 리스트에 담기
                일자리정보=[회사명,공고명,경력,학력,계약유형,지역,채용기간] ; #print(일자리정보)
                result.append(일자리정보)
        else:
            print('>>통신실패')
    return result

#[2]2차원 리스트를 csv 변환해주는 서비스 , 데이터 , csv파일명 , 열(제목) 목록
def list2d_to_csv(result, fileName,colsNames):
    try:
        df=pd.DataFrame(result,columns=colsNames)
        df.to_csv(f'{fileName}.csv',encoding='utf-8',mode='w')
        return True
    except Exception as e:
        print(e)
        return False

#[3] csv 파일을 JSON 형식의 PY타입으로 가져오기
def read_csv_to_json(fileName):
    #1. 판다스를 이용한 csv를 데이터프레임으로 가져오기
    df=pd.read_csv(f'{fileName}.csv',encoding='utf-8',engine='python',index_col=0)
    # 2. 데이터프레임 객체를 JSON 으로 가져오기
    jsonResult=df.to_json(orient='records',force_ascii=False)
    result=json.loads(jsonResult)
    return result

#[4] 총채용 공고수,경력별 공고수,학력별 공고수 출력하기
def announcement_number(result):
    totalEmployment=len(result)  #총채용 공고수
    print(totalEmployment)








# # 서비스 테스트 확인 구역
# if __name__ == "__main__" :
#     result=[]
#     jobkoreaInfo(result);
#     print(result)
    # list2d_to_csv(result,'잡코리아일자리정보',['회사명','공고명','경력','학력','계약유형','지역','채용기간'])
    # result2=read_csv_to_json('잡코리아일자리정보')
    # print(result2)

