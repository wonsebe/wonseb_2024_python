#t.정리.txt.py

#독립표본검증 : 두 개의 독립된 그룹의 평균을 비교
    #예] 남성과 여성의 평균 키 비교
#대응 표본 정리.txt: 동일한 그룹에서 두 시점의 평균을 비교
    #예] 다이어트 전/후의 체중비교
#단일 표본 정리.txt: 하나의 표본 평균이 알려진 모집간 평균과 다른지 비교

#[1] 성별 별로 스포츠 선호도 조사
    #설문조사를 통해 귀하는 (1) 1. 남자 2. 여자 (명목형)  (2) 수스포츠 선호도 점수 0 1 2 3  4 5 6 7 8 9

#[2] 데이터 수집
남자스포츠선호도=[7,8,9,6,7]
여자스포츠선호도=[5,6,4,7,5]
#[3]모듈 호출
import scipy.stats as stats
#[4] t검증의 독립 표본 정리.txt
t통계량 , p값=stats.ttest_ind(남자스포츠선호도, 여자스포츠선호도)
#[5] 확인
print(t통계량)
# 두 집단의 평균차이를 표준화한 값
# 분석 : 이 값이 클수록 차이가 있다는 뜻
    #음수는 첫번째 집단의 평균이 두번째 집단보다 낮다는 뜻
    #양수는 첫번째 집단의 평균이 두번째 집단보다 높다는 뜻
print(p값)
# 5% 버리고 보편적인 데이터를 가지고 결론 낸다. 일반적으로 통계학에서 사용되는 방법
# 일반적으로 p값이 0.05보다 작으면 귀두가설을 기각해서 해당 통계/분석은 충분한 근거/효과 있다.