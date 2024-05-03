'''
13.  월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요.
- 월(Month)에 해당하지 않는 숫자 입력 시 “잘못된 데이터입니다” 출력

'''
monSeason = {"1" : "Jan Winter",
             "2" : 'Fab Winter',
             "3" : "Mar Spring",
             "4" : "April Spring",
             "5" : "May Spring",
             "6" : "June Spring",
             "7" : "July Summer",
             "8" : "August Summer",
             "9" : "September Summer",
             "10" : "October Fall",
             "11" : "November Fall",
             "12" : "December Winter"}
mon = input("좋아하는 월 입력 : ")
print(monSeason[mon] if mon in monSeason.keys() else "존재하지 않는 월입니다.")