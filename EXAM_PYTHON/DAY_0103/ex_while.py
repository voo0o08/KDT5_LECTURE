'''
comprehension
- list, dict, set에 가능
'''
# [실습] aList의 원소 값을 제곱한 값을 원소로 가지는 blist 생성하세요.
aList = [1, 2, 3, 4]

bList = []
for a in aList:
    bList.append(a**2)
print(f"bList = {bList}")

# comprehension으로 짝수만 담기
cList = [a ** 2 for a in aList if not a % 2]
#          (3)       (1)           (2)
# (2)에서 True인 경우만 (3)실행
print(f"cList = {cList}")

# [실습3] aList의 원소 값 중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로인 bList 생성
print(f"\n실습3 aList = {aList}")
bList = []
for a in aList:
    if not a%2:
        bList.append(a**2)
    else:
        bList.append(a)
print(f"bList = {bList}")

bList = [a**2 if not a % 2 else a for a in aList]
#        ---- ------------ ------ --------------
#         3T       2         3F         1
print(f"bList = {bList}")
