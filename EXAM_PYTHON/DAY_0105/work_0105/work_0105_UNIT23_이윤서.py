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
