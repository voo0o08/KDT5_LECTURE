# 반복문과 내장함수
xList = ["1", "3", "5", "7"]

# xList안에 모든 원소를 정수 int로 변환 후 저장해 주세요~
xList = map(int, xList)
xList = map(str, xList)

# list 데이터를 dict 데이터로 생성
x = ['st01', 'st02', 'st03']
y = [90, 100, 99]

xyDict = dict(zip(x, y))
print(xyDict)

# 다른 방법
xy = []
for idx in range(len(x)):
    xy.append((x[idx], y[idx]))

print(dict(xy))