# ppt 141p
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드라고 부름
# -범용의 함수와 식별하기 위해서 지정한 호칭
# -사용법 : 데이터.메서드명 / 변수명.메서드명

# List 전용 메서드 살펴보기
nums = []
print(f"리스트 요소 개수 {len(nums)}개") # 0개

# add / append / insert

nums.append("어펜드~") # 무조건 마지막에 들어감
print(nums)

nums.insert(1, ["ABC", "DEF"]) # index, object
print(nums)

del nums[-1][1]
print(nums)

# 리스트 내의 모든 원소 삭제하기
del nums[:]
print(nums)

# 리스트 안에 원소/요소 정렬해주는 메서드 => sort() 오름차순 정렬
# 작은 데이터부터 등장
print("\nsort method")
nums = [95,3, 45, 7, 64]
nums.sort()
print(nums)
# 내림차순
nums.sort(reverse=True)
print(nums)

# 리스트 안에 위치들을 반대로 뒤집는 메서드, 비교x, 순서만 변경
print("\nreverse method")
nums.reverse()
print(nums)

# 리스트 안에 원소/요소를 삭제해주는 메서드 => remove(데이터)
# del은 인덱스를 줘야하고 remove는 데이터를 줘야함
print("\nremove")
nums.remove(64) # nums.remove(nums[?])으로 해도 ㅇㅋ
print(nums)

# clear는 전체 삭제
print("\nclear()")
nums.clear()
print(nums)

# 리스트 원소/요소를 꺼내는 메서드 => pop()
# 아무것도 안넣으면 마지막 요소 <-> append 반대개념
nums = [0, 1, 2, 3, 4, 5]
print("\npop()")
nums.pop() # 저장 가능 None아닌 값이 나옴
nums.pop(0)
print(nums)

# 리스트에서 특정 원소/요소 데이터가 몇 개 존재하는지 => count()
nums = [0, 0, 0, 34, 56, 789, 45, 'A', 'A', 'A']
print("\ncount")
print(nums.count("A"))
print(nums.count(0))

# 리스트를 확장시켜주는 메서드 => extend(여러 개의 데이터를 저장한 타입)
nums = [1, 2, 3]
nums.extend([4, 5, 6])
print("\nextend(어쩌구)")
print(nums)
print([1, 2, 3] + [4, 5, 6])
nums.extend("안녕하세요오...")
print(nums)
# nums.extend(24) # 놉 순서형 자료만 가능

# 리스트를 복사해주는 메서드 => 얕은 복사 copy()
print("\ncopy()")
nums.append([100, 200])
nums2 = nums.copy()
nums2[-2] = 2024
print(nums)
print(nums2,"\n")

nums2[-1][0] = 77
print(nums)
print(nums2,"\n")
