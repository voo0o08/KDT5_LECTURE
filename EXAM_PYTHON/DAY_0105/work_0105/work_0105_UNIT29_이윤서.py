# 29.7 연습문제: 몫과 나머지를 구하는 함수 만들기
x = 10; y = 3
def get_quotient_remainder(n1, n2):
    return n1//n2, n1%n2
quotient, remainder = get_quotient_remainder(x,y)
print("몫: {0}, 나머지: {1}".format(quotient, remainder))

# 29.8 심사문제: 사칙 연산 함수 만들기
'''
숫자 두개 공백 입력
사칙 연산 결과 출력
'''
# x, y = map(int, input().split())
# def calc(n1, n2):
#     return n1+n2, n1-n2, n1*n2, n1/n2
# a, s, m, d = calc(x, y)
# print("덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}".format(a, s, m, d))

print("안녕하 세 요.".replace(" ",""))