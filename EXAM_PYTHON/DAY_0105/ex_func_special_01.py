'''
다양한 함수의 형태 - 특별한 함수 (1)
- 매개변수의 개수가 유동적으로 가변되는 함수
- 형태 : def 함수명(*data):
- 가변 인자 함수
- 매개변수 개수 : 0개 ~ N개
* 은 언패킹 *(리스트/range/튜플)
** 은 딕셔너리 웁싀~
'''
# 2개 정수를 덧셈 후 결과 반환
# def addNum(n1, n2, n3, n4, n5):
#     return n1+n2+n3+n4+n5
#
# print(addNum(1, 2, 3, 4, 5))

# print(lambda x, y: x+y)

'''
함수 기능 : 전달 받은 숫자를 모두 덧셈한 결과 반환 기능
함수 이름 : addNumber
매개 변수 : *nums
반 환 값 : 계산 결과
'''
def addNumber(*data):
    ret = 0
    for d in data:
        ret += d
    return ret

# print(addNumber(1,2,3))
# print(addNumber())
# print(addNumber(10))
print(addNumber(*(range(1, 11))))
a = [1, 2, 100]
print(addNumber(*a))
aTuple = "a", "b", "c"
print(aTuple)
print(*aTuple)
print()

aDict = {"my_name":"Hong", "age":100}
print(*aDict) # Key 값 가져와줌 **도 되지만 print가 **을 안받아서 나중에 사용ㄲ

