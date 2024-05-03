'''
4. 아래 조건을 만족하는 코드를 작성하세요.
- 수의 범위 : 1 ~ 100
- 3의 배수 숫자
- 7의 배수 숫자
- 8의 배수 숫자
- 3, 7, 8의 배수 숫자로 구성된 숫자만 출력
- 단!! 중복된 숫자는 제거 하세요
'''
numList = list(range(1, 101))
result = []
for num in [3, 7, 8]:
    for i in range(num-1, 101, num):
        result.append(numList[i])
print(set(result))