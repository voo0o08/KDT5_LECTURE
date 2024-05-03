# [실습1] 알고 싶은 단을 입력 받고 해당 단을 출력
# input()
# 특정 단의 구구단을 출력 => 반복문 사용하기
'''
num = input("알고 싶은 단 : ")

# for i in range(1, 10):
#     print(f"{num} * {i} = {num*i:2}")

if num.isdecimal():
    num = int(num)
    for i in range(9, 0, -1):
        print(f"{num} * {i} = {num*i:2}")
else:
    print("정확한 데이터가 없습니다.")
'''
# [실습2] 2단 ~ 9단까지 모두 출력
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} * {i} = {i*j}", end="\n" if j == 9 else "\t")

# 모범답안
for num in range(10):
    for dan in range(2, 10):
        if num:
            print(f"{dan} * {num} = {dan*num:2}", end="\n" if dan == 9 else "\t")
        else:
            print(f"---{dan}단---", end="\n" if dan == 9 else "\t")
