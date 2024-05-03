# # 17.6 심사문제: 교통카드 잔액 출력하기
# '''
# 표준입력 : 금액(int)
# 1회당 요금 1350
# 교통카드 사용 잔액 출력 프로그램
# 최초 금액 출력 x
# 잔액부족 -> break
# '''
# bal = int(input())
# while True:
#     if bal-1350 < 0:
#         break
#     print(bal-1350)
#     bal -= 1350

# # 18.5 연습문제: 3으로 끝나는 숫자만 출력하기
# '''
# - 0~73 사이
# '''
# i = 0
# while True:
#     if i > 73:
#         break
#     if str(i)[-1] == "3":
#         print(i, end=" ")
#     i += 1
#
# # 18.6 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
# '''
# - 공백 두고 정수 2개
# '''
# print()
# start, end = map(int, input().split())
#
# i = start
# while True:
#     if i > end:
#         break
#     if str(i)[-1] != "3":
#         print(i, end=" ")
#     i += 1

# # 20.7 연습문제: 2와 11의 배수, 공배수 처리하기
# for i in range(1, 101):
#     if i % 2 == 0 and i % 11 == 0:
#         print('FizzBuzz')
#     elif i % 2 == 0:
#         print('Fizz')
#     elif i % 11 == 0:
#         print('Buzz')
#     else:
#         print(i)
#
# # 20.8 심사문제: 5와 7의 배수, 공배수 처리하기
# '''
# 첫번째 정수부터 두 번째 정수까지 숫자를 출력
# 5 = Fizz / 7 = Buzz / 5 and 7 = FizzBuzz
# '''
# num1, num2 = map(int, input().split())
#
# for i in range(num1, num2+1):
#     if i % 5 == 0 and i % 7 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Fizz')
#     elif i % 7 == 0:
#         print('Buzz')
#     else:
#         print(i)

# 23.6 연습문제: 3차원 리스트 만들기
'''
높이 2 / 세로 4 / 가로 3인 3차원 리스트 만들기
'''
a = [[[0 for i in range(3)] for i in range(4)] for i in range(2)]
print(a)

# 23.7 심사문제: 지뢰찾기
'''
표준 입력으로 2차원 리스트의 col, row가 입력
리스트의 요소로 들어갈 문자 입력
*은 지뢰/.은 지뢰x
지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력할 것
.**
*..
.*.
'''
# col, row = 5, 5
# L = [['.', '.', '*', '.', '.'], ['.', '.', '.', '*', '.'],
#      ['.', '*', '.', '.', '.'], ['.', '*', '*', '*', '.'],
#      ['*', ".", '*', '.', '.']]
# col, row = 3, 3
# L = [['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]
col, row = map(int, input().split())
L = []
for i in range(row):
    L.append(list(input()))
print(L)
for i in range(row):
    for j in range(col):
        if L[i][j] == "*": continue
        count = 0
        for y in range(max(i-1, 0), min(row, i+2)):
            for x in range(max(j-1, 0), min(col, j+2)): # 가로(col) 체크(세로 고정)
                if L[y][x] == "*":
                    count += 1
        L[i][j] = count
print(L)
