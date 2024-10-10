#1_카이검증.py

# day15 --> 1_카이검증.py
# 카이검증이란?
#   (독립성검증) 두 변수간의 독립성을 정리.txt
#       예] 성별과 선호하는 제품 유형 간의 연관성
            # 1. 설문조사 : 1.남자 2.여자       ( 명목형 변수 )
            # 2. 설문조사 : 1.텔레비전 2.컴퓨터  ( 명목형 변수 )
#   (적합성검증) 관찰된 빈도 분포가 예상된 분포와 얼마나 일치하는지 정리.txt
#       예] 주사위를 여러번 굴렀을때 나오는 빈도가 이론적으로 예상되는 빈도와 일치하는지 확인

#[1] 성별 별로 컨텐츠 선호도 조사
# 설문조사를 통해 귀하는 (1)1.남자2.여자 (명목형)   (2) 1.스포츠 2.드라마 (명목형)

#[2] 자료 수집
''' - 설문조사 결과
            스포츠     드라마
    남       50명       30명
    여       20명       40명
'''
설문결과 = [  [ 50 , 30 ]  ,
            [ 20 , 40 ] ]
# [3] 모듈 호출
import scipy.stats as stats
# [4] 카이 정리.txt
통계량 , p값 ,  자유도 , 기대빈도표 = stats.chi2_contingency( 설문결과 ) # contingency 유연성 뜻
# [5] 카이 정리.txt 결과
print( 통계량  ) # 10.529166666666667
print( p값 ) # 0.0011750518530845063
print( '성별과 컨텐츠 선호도가 독립적일때 예상되는 빈도표')
print( 기대빈도표 )
