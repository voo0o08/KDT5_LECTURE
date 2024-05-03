'''
수치 데이터 살펴보기
- 정수 => class int
- 실수 => class float
- 복소수 => class complex
'''

a = 0b1010 # 2진수
b = 0o127 # 8진수
c = 0x7F # 16진수

# [실습] 2개의 정수를 입력 받기
# -> input() 함수 2개 사용
# -> str => int 타입 캐스팅
num1 = int(input("숫자 1개 입력 : "))
num2 = int(input("숫자 1개 입력 : "))

# 비교연산 결과 출력
print("%d>%d = %s" %(num1, num2, num1>num2))

