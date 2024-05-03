def currentDate(todays):
    # todays => 년, 월, 일을 원소로 담고 있는 데이터 타입(리스트)
    print(f"Tody : {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}")

def currentDate2(month, day):
    global year
    year += 10
    print(f"Tody : {year}/{month:0>2}/{day:0>2}")

# 전역변수
year, month, day = 2024, 1, 8
todayList = [year, month, day]

# 함수 사용 즉 함수 호출 ---------------
currentDate(todayList)

# 변수 값 확인 출력
print(f"year : {year}, month : {month}, day : {day}")

