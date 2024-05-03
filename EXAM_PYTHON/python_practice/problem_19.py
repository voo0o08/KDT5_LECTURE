'''
19. 팩토리얼(Factorial)을 while반복문으로 구현해 주세요.
 팩토리얼 수를 입력 받아서 팩토리얼 결과를 아래와 같이 출력하세요.
'''
num = int(input("팩토리얼 수 입력 : "))
msg = f"{num}! => "
result = 1

while num:
    result *= num
    msg += f"{num} =" if num == 1 else f"{num} * "
    num -= 1
print(msg, result)