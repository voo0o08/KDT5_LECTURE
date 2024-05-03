# -------------------------------------------
# dict 데이터 전용 함수 즉, 메서드
# -------------------------------------------

myDict = {}

# 데이터 추가 => myDict[key] = data
myDict['one'] = 100

# 데이터 추가 => update(key = data)
# update => key는 str타입만 가능, '', "" 사용 안됨
myDict.update(two = 200)
print(myDict)

# 키만 추출해서 읽어오는 메서드 => keys() 메서드 ----
keys = myDict.keys()
print(keys, type(keys))

# 값만 추출해서 읽어오는 메서드 => values() 메서드 ----
values = myDict.values()
print(keys, type(values))

# 원소/요소 단위 접근 위해서는 형변화 필요함!!
items = list(myDict.items())


# 키와 값을 가져오는 메서드 => items() -> 튜플 형식으로 묶여 나옴
items = myDict.items()
print(items, type(items))

# 모두 삭제해주는 메서드 => clear()
# myDict.clear()

# 원소/요소 데이터 읽기 메서드 => 변수명[키] ==> 값, get(키) 메서드
print(myDict.get("one")) # 없으면 None
print(myDict["one"]) # 없으면 Error

# 멤버 연산자 in ~ / not in ~
# ~는 str, list, tuple, dict, set
# 연산 결과 = T / F
aList=[1, 2, 3]
aTuple = 11, 22
aDict = {1:100, 2:100}
print(f"1 in aList : {1 in aList}")
print(f"1 in aTuple : {1 in aTuple}")
print(f"1 in aDict : {1 in aDict}") # key 존재 여부