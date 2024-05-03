'''
tuple과 list
'''

myData = (10, 20, ["hong", 30], ('Kim', 12)) # 여러 종류의 데이터 가능

# 튜프르이 원소/요소 개수 확인 => len()
print(f'myData의 원소 수{len(myData)}개')
# 인덱스 범위
print(f'myData 인덱스 범위 : 0 ~ {len(myData)-1}')

# 튜플에서 원소/요소 데이터 읽기
print(f"myData : {type(myData[2])}")
print(f"myData : {type(myData[3])}")

# 튜플에서 0번째 원소의 데이터를 변경하기
myData[2][0] = "Park" # 이렇게 접근하면 튜플이 아닌 리스트로 접근됨
print(myData)

# tuple과 연산
print("\ntuple연산")
# 1~10 범위에서 2의 배수로 구성된 정수 튜플 1개
t1 = tuple(range(2,11,2))
print(t1)
# 1~10 범위에서 5의 배수로 구성된 정수 튜플 1개
t2 = tuple(range(5,11,5))
print(t2)
print(t1+t2) # 원소변경x