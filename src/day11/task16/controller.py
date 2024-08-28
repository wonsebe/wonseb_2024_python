#controller.py

#[1] 플라스크 객체 가져오기
from appstart import app
#[2] (우리가 만든 ) 서비스 모듈 가져오기
import service

#4. app,run 코드 위에 HTTP 매핑 주소 정의
@app.route('/job',methods=['get'])
def getjob():
    result=[]
    service.jobkoreaInfo(result)
    service. list2d_to_csv(result,'잡코리아일자리정보',['회사명','공고명','경력','학력','계약유형','지역','채용기간'])
    result2 = service.read_csv_to_json('잡코리아일자리정보')
    #채용별 공고수
    service.announcement_number(result)
    # service.announcement_number(result)
    return result2