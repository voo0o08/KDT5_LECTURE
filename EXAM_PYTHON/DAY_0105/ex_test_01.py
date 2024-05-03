'''
[실습1] 2개의 정수를 입력 받은 후 사칙 연산 수행 결과를 반환하는 기능의 함수를 정의
함수 이름 : fourCalc
매개 변수 : n1, n2
반 환 값 : 계산 결과

'''
def fourCalc(x, y):
    return x+y, x-y, x*y, x/y
pls,mns,mul,dvd = fourCalc(1, 3)

'''
[실습2] 문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의해 주세요.
함수 이름 : getCode
매개 변수 : message
반 환 값 : str
'''
def getCode(message):
    msgList = list(message)
    result = ""
    for idx, ch in enumerate(msgList):
        msg2hex = hex(ord(ch))
        result += (msg2hex[2:] + " ")
    return result

print(getCode("hello"))
