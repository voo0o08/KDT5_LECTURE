
'''
2. 키보드로 입력 받은 데이터 중에서 숫자만 모두 저장하여 합계, 최대값, 최소값을
 출력하는 함수를 구현하세요.
하늘 Apple 2021 -9 False 23 7 None 끝
A 홍길동 False True True None Good Luck 가나다라
'''
datas = input("데이터 입력 : ").split()
numList = []
for data in datas:
    if not (data.isalpha()):
        numList.append(data)
numList = [int(num) for num in numList]
if not(len(numList)):
    numList.append(0)
print(f"합계 : {sum(numList)} 최댓값 : {max(numList)} 최솟값 : {min(numList)}")
