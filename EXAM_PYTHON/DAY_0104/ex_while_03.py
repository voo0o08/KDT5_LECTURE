'''
- 반복의 횟수가 정해지지 않은 경우
'''
# [요청] 사용자가 'x'입력 전까지 입력 받은 데이터를 저장해 주세요.
# => 몇 번 입력할지 알 수 없음 => 무한 입력 받기로 설정
while False:
    data = input("저장하고 싶은 데이터 입력(종료는 x) : ")
    # 종료 검사 => break : 키워드가 있는 부분에서 반복 종료, 아래코드 실행 안됨
    # if data == "x" or data == "X":
    if data in ("x", "X"):
        break
    print(data)
    print("OK")

# [요청] 사용자로 부터 x/X 입력 전까지 계속 정수를 입력
# 입력받은 정수만큼 알파벳 출력
# 출력 원하는 알파벳 수 입력 : 5

while False:
    num = input("출력 원하는 알파벳 수 입력 : ")

    if num in ("x", "X"):
        break
    else:
        num = int(num)

    start = ord("a")
    i = 1
    while i <= num and start <= ord("z"):
        print(chr(start), end="")
        start += 1
        i += 1
    print()

#
# aCode = ord("a")
# for value in range(5):
#     value += aCode
#     print(f"value => {value}, {chr(value)}")


while True:
    count = input("출력 원하는 알파벳 수 : ")
    if count in ("x", "X"):
        print("프로그램이 종료됩니다.")
        break

    if count.isdecimal():
        count = int(count)
        aCode = ord("A")
        for val in range(count):
            val += aCode
            print(f"value => {val}, {chr(val)}")
            if val == ord('Z') : break
    else:
        print("유효한 데이터가 아닙니다.")

# [요청] 내부에 반복문에서 데이터가 10을 넘으면 프로그램 종료
# for문 ver
isEnd = False
for n in range(100):
    if isEnd == True:
        print("프로그램 종료")
        break
    print(f"out -> {n}")
    for n2 in range(100):
        if n2>10 :
            isEnd = True
            break
        print(f"in -> {n2}")

# while문 ver으로 만들기
print("\n\nwhile문 ver")
i, j = 0, 0
end = False
while i < 100:
    if end:
        print("프로그램 종료")
        break
    print(f"out -> {i}")
    j = 0
    while j < 100:
        if j > 10:
            end = True
            break
        print(f"in -> {j}")
        j += 1
    i += 1

