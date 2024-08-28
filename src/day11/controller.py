#controller.py

#[1] 플라스크 객체 가져오기
from appStart import  app
#[2] ( 우리가 만든 )서비스 모듈 가져오기
import service



 #4. app.run 코드 위에 HTTp 매핑 주소 정의
@app.route('/qooqoo',methods=['get'])
def getqooqoo():
    result=[]
    service.qooqooStoreInfo(result)#크롤링해서 csv파일 생성
    service.list2d_to_csv(result, '전국쿠우쿠우매장', ['번호', '지점명', '연락처', '주소', '영업시간'])
    #(2) CSV 에 저장된 JSON 으로 가져오기
    result2=service.read_csv_to_json('전국쿠우쿠우매장')
    #(3) 서비스로부터 받은 데이터로 HTTP 응답하기
    return result2
