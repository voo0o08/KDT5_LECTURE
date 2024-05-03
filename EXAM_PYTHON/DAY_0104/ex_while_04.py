'''
continue = 계속해서~
- 키워드 아래 코드 실행 안됨
- 반복 상단으로 이동
'''
numList = list(range(1, 31))

for data in numList:
    if not data%2:
        print(data)

for data in numList:
    if data%2:
        continue
    print(data)

# while------------------------------
print("\ncontinue없는 ver")
idx = 0
while idx<30:
    if numList[idx] % 2 == 0:
        print(numList[idx])
    idx += 1

print("\ncontinue ver")
idx = -1
while idx<29:
    idx += 1
    if numList[idx] % 2 != 0:
        continue
    print(numList[idx])
