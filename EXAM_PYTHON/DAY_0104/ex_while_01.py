'''
반복문 - 2 while
- 반복의 횟수가 정해지지 않고, 조건에 따르는 경우
- 반복의 횟수가 정해진 경우에도 사용 가능함
'''
TEST = False # Flag변수
# [ 요청 ] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
# 단, 사용자가 끝이라는 음식명 입력 전까지 입력 받으세요
# 몇 번 입력 받아야 입력이 끝날지 알 수 없음


# [ 요청 ] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
# 단, 가장 좋아하는 음식 5개만 입력
# => 사용자의 Top5 음식명 출력
if TEST:
    foods = [input("좋아하는 음식 : ") for i in range(5)]
    print("당신은", end=" ")
    for food in foods:
        print(food, end=", " if foods[-1] != food else " ")
    print("를 좋아하는군요!")

    strfoods = ""
    for i in range(5):
        food = input("좋아하는 음식:")
        strfoods = strfoods + food+", " if i != 4 else strfoods + food
    print(strfoods)

    # foods = []
    # for i in range(5):
    #     foods.append(input("좋아하는 음식을 작성해주세요. : "))
    # print(foods)

# 기본 while 문법
# while 조건식:
# 타이머 프로그램 만들기 => 다운카운팅 10 9 8 7 6 5..
downCnt = 10
while downCnt:
    print(downCnt)
    downCnt -= 1

# 업카운팅
upCnt = 1
while upCnt < 11:
    print(upCnt)
    upCnt += 1

# for 문으로 count하기
print("\nfor-upcount")
for i in range(1, 11):
    print(i,end=" ")

print("\nfor-downcount")
for i in range(10, 0, -1):
    print(i,end=" ")