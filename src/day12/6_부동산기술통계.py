#부동산기술통계.py

# [3] 데이터 탐색(기술통계)
    # 전체 기술통계 결과를 SPRING index6.html 테이블형식으로 출력  ( HTTP 매핑 임의로 정의 )
# [4] 데이터 모델링( 그룹화 )
    # 전월세 기준으로 그룹해서 전용면적의 기술통계 결과를 SPRING index6.html 테이블형로식으 [3]번 테이블 위에 출력  ( HTTP 매핑 임의로 정의 )

# [5] 추가
    # 1. 부평구의 동 명을 중복없이 출력하시오.
    # 2. 가장 거래수가 많은 단지명 을 1~5 등까지 출력하시오.

# 카카오톡방에 ip 제출
#모듈 가져오기
import pandas as pd
from flask import Flask
import json

#Flask 객체 생성
start=Flask(__name__)
#HTTP GET 매핑 설정
Apartment_sale_pd = pd.read_csv('아파트(전월세)_실거래가_20240829163501.csv', encoding='cp949', engine='python', index_col=0)
# print(Apartment_sale_pd)
Apartment_sale_pd.columns = Apartment_sale_pd.columns.str.replace(' ', '_')
# print(Apartment_sale_pd.head())
aparment=Apartment_sale_pd.describe(); print(aparment)
jsonResult=Apartment_sale_pd.to_json(orient='records',force_ascii=False)
result = json.loads(jsonResult)


@start.route('/as',methods=['get'])

def getApartmentSales():
    return  result

if __name__=="__main__":
    start.run(host='0.0.0.0', debug=True)











