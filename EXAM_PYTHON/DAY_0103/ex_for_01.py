# 1~100 사이에서 2의 배수에 해당하는 정수로 리스트 생성
L = list(range(2, 101, 2))
print(L)

# 시퀀스 데이터 타입에서 원소/요소를 하나씩 빼서 반복 코드 수행 => for in

strNum = ''
for num in L:
    strNum = strNum + str(num)
print(f"strNum => {type(strNum)}\n{strNum}")

# 인덱스 범위 => 0~len(data)-1
range(len(L))
print(f"before => {L}")
for idx in range(len(L)):
    L[idx] = str(L[idx])


print(f"result => {L}")

