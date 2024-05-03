# 함수 기능 : 팩토리얼 함수 반들기
# 함수 이름 : fac
# 매개 변수 : num
# 반 환 값 : 팩토리얼 결과

def fac(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
print(fac(3))

def fact(x):
    if x == 0:
        return 1
    while x:
        print(f'{x}! = {x}*{x-1}')
        return x*fact(x-1)
print(fact(3))

# 팩토리얼 계산 후 아래 형태로 반환
# 3! : 3 * 2 * 1 = 6
print()
def fac(num):
    print(f"{num}! : ",end="")
    result = 1
    for i in range(num, 0, -1):
        print(f"{i} *" if i > 1 else f"{i}", end=" ")
        result *= i
    print(f"= {result}")
    return result
print(fac(5))
