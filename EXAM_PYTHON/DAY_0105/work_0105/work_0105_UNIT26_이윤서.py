'''
26.8 연습문제: 공배수 구하기
'''
a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

print(a & b)

'''
26.9 심사문제: 공약수 구하기
'''
user = "10 20"
num1, num2 = map(int, user.split())
a = set(); b = set()
for i in range(1, num1+1):
    if num1 % i == 0:
        a.add(i)
for i in range(1, num2+1):
    if num2 % i == 0:
        b.add(i)

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)