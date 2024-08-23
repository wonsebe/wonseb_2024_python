# day07 > task9 > region.py
class Region :
    #생성자
    def __init__(self,name,total,male,female,house):
        #self: 자기 자신(객체)
        self.name=name
        self.total = total
        self.male = male
        self.female = female
        self.house = house

        #메소드, 남자 백분율
        def malePercent(self):
            return round((self.male/self.total)*100,1)
        #메소드 , 여자 백분율
        def femalePercent(self):
            return round((self.female/self.total)*100 ,1)
        #toString, 객체 변수 정보 출력
        def toString(self):
            return f'{self.name:<10}{self.total:>10}'


