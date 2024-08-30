#0_저번시간아파트매매.py
import json
import pandas as pd
from flask import Flask
app=Flask(__name__)
#[4] CORS 허용
from flask_cors import CORS
CORS(app)
df=pd.DataFrame()
for year in range(2022,2025):   #2022~2024
    df2=pd.read_csv(f'{year}.cvs ' , encoding='cp949', skiprows=15)
    print(df2.shape)

df= pd.read_csv('아파트(전월세)_실거래가_20240830102805.csv',encoding='cp949')

    #1
@app.route('/trans1',methods=['get'])
def trans1():
    return json.loads(df.describe().to_json())
    #2
@app.route('/trans2',methods=['get'])
def trans2():
    return json.loads(df.groupby('전월세구분')['전용면적(㎡)'].describe().to_json())
    #3
@app.route('/trans3',methods=['get'])
def trans3():
    return list( df['시군구'].unique() )
    #4
@app.route('/trans4',methods=['get'])
def trans4():
    return json.loads(df['단지명'].value_counts().head().to_json())

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)


    #encoding='utf-8' 기본값(생략시) 안될경우 cp949
    # skiprows=몇번째 행까지 스킵행번호: 특정 행을 제외한 csv 읽어오기
# print( df )
# 1. 통계 # describe()
# print( df.describe() ) # count(개수) , mean(평균) , std(편차) , min(최소값) , max(최대값) , 25%백분위수 , 50%백분위수 , 75%백분위수
# print( df.describe().to_json() ) # JSON 형식의 문자열 변환
print( json.loads( df.describe().to_json() ) ) # JSON 형식의 문자열 타입을 딕셔너리(PY타입) 변환 # 플라스크의 HTTP 응답시 전송하기 위해서
# 2. 그룹화 통계
# print( df.groupby('전월세구분')['전용면적(㎡)'].describe() )
print( json.loads( df.groupby('전월세구분')['전용면적(㎡)'].describe().to_json() ) )
# 3. 중복제거
# print( df['시군구'] ) # df 에서 특정 열만 추출
print(  df['시군구'].unique() ) # (중복값을 제거한) 특정 열만 추출
# 4. 레코드 수
# print( df['단지명'].value_counts() ) # df 에서 특저 열의 레코드(행) 수
# print( df['단지명'].value_counts().head() ) # df 에서 위에서 5개만 추출 .head()
print( json.loads(  df['단지명'].value_counts().head().to_json() ) )