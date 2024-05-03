'''
함수와 클래스
변수에 어떤 데이터를 저장하고 있는지 확인하는 함수 -> type(변수명)
'''
data = 1
print(f"data Type => {type(data)}")

data = "Good"
print(f"data Type => {type(data)}")

# 함수명의 타입
print(f"id()함수의 Type => {type(id)}") # 주의할 점 id()가 아닌 id. 즉, 함수의 이름만 작성해야함

# 함수는 내장함수/사용자정의함수로 구분됨
# 사용자 정의 함수 생성
# 함수 기능 : 2개 정수 더한 후 결과 출력 기능
# 함수 이름 : addTwo
# 매개 변수 : n1, n2
# 함수 결과 : 없음
def addTwo(n1, n2):
    print(n1+n2)

# 함수의 타입 출력 => type() 내장함수 사용 => class function
print(f"addTwo()함수의 Type => {type(addTwo)}")

# 결론 : 파이썬은 모든게 class로 이루어져 있음
print()
# 함수와 변수
# - 함수명은 코드의 시작주소를 저장하고 있음 -> 함수명을 변수에 대입 가능
test = addTwo # 마찬가지로 ()를 넣으면 호출이기 때문에 괄호 없이 함수 이름만 담기
print(f"test => {id(test)}, {type(test)}")
print(f"addTwo => {id(addTwo)}, {type(addTwo)}")
test(20, 30)
addTwo(20, 30)
print()

'''
[활용 예]
- 1~10 범위에서 임의의 정수 5개를 저장
- 중복된 정수 저장 가능
'''
import random
numList = [random.randint(1, 10) for i in range(5)]
print(numList)

# 5개의 정수에서 최대값, 최소값, 내림차순 정렬된 값의 결과를 출력하기
print(f"최대값 : {max(numList)}, 최소값 : {min(numList)}, 내림차순 정렬된 값 : {sorted(numList, reverse=1)}")

print()

funs = [max, min, sorted, sum, len]
for f in funs:
    if f == sorted:
        print(f(numList, reverse=True))
    else:
        print(f(numList))

print()

funDict = {"최대값" : max, "최소값" : min, "정렬" : sorted, "합계" : sum, "개수" : len}
for key, val in funDict.items():
    if key == "정렬":
        print(val(numList, reverse=True))
    else:
        print(val(numList))