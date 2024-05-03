'''
31. 입력된 년도가 윤년인지 평년인지 평가하는 코드를 구현하세요.
'''
def leapYear():
    year = int(input("년도 입력 : "))
    if year % 4 ==0 and year % 100 == 0:
        result = "평년"
    elif not(year % 400) or not(year % 4):
        result = "윤년"
    print(f"{year}년은 {result}입니다.")
leapYear()
