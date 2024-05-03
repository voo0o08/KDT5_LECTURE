'''
22.9 연습문제 : 리스트에서 특정 요소만 뽑아내기
'''
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]

print(b)

'''
22.10 심사문제: 2의 거듭제곱 리스트 생성하기
표준 입력 정수 2개
거듭제곱 리스트 출력 프로그램
'''
num1, num2 = map(int, input().split())
print([2 ** i for i in range(num1, num2+1)])