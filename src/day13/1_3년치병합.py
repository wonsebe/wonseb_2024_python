#.1_3년치병합.py

import pandas as pd
import json
from flask import Flask
app=Flask(__name__)
from flask_cors import CORS
CORS(app)
df_2022=pd.read_csv('아파트(전월세)_실거래가_20240830120247_2022.csv',encoding='cp949')
df_2023=pd.read_csv('아파트(전월세)_실거래가_20240830120436_2023.csv',encoding='cp949')
df_2024=pd.read_csv('아파트(전월세)_실거래가_20240830120526_2024.csv',encoding='cp949')
# print(df_2022.head())
# print(df_2023.head())
# print(df_2024.head())
@app.route('/start',methods=['get'])
def start():
    return json.loads(df.to_json())
#3. 두 데이터프레임 합치기
df=pd.concat([df_2022,df_2023,df_2024])
# print(df.shape)

#4. 합친 와인 데이터프레임 ---> csv 파일로 저장
df.to_csv('df.csv',index=False)
#1. 데이터프레임의 기존정보 출력
# print(df.info())
# print(df.describe())
# df.columns=df.columns.str.replace(' ','_')

# print( json.loads( df.describe().to_json() ) ) # JSON 형식의 문자열 타입을 딕셔너리(PY타입) 변환 # 플라스크의 HTTP 응답시 전송하기 위해서
df.reset_index(drop=True, inplace=True)


if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True)



