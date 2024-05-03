
def currentDate2(month, day):
    # month, day => 지역변수
    # year => 전역변수
    year += 10
    print(f"Tody : {year}/{month:0>2}/{day:0>2}")

# 전역변수
year, month, day = 2024, 1, 8

# 함수 사용 즉 함수 호출 ---------------
currentDate2(month, day, "Friday")


