
'''
28. 6가지 연산 결과를 한꺼번에 반환하는 함수를 생성 후 호출하여 결과를 아래와 같이
 출력해 주세요.
- 6가지 연산 : 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지값, 몫
'''
def calc():
    num1, num2 = map(int, input("숫자 2개 입력 (3, 4) : ").split(","))
    print(f"덧셈 결과 : {num1+num2}")
    print(f"뺄셈 결과 : {num1-num2}")
    print(f"곱셈 결과 : {num1*num2}")
    print(f"나누기 결과 : {num1/num2 if num2 else 0}")
    print(f"몫 결과 : {num1//num2 if num2 else 0}")
    print(f"나머지 결과 : {num1%num2 if num2 else 0}")
calc()