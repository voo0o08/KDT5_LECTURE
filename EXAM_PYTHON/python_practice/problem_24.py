
'''
24. 입력받은 숫자에서 천자리, 백자리, 십자리, 일자리를 출력하세요.
- 입력은 함수에 포함하지 않음
- 숫자에서 자리 수를 출력하는 함수 구현
'''
def numWhere(num):
    numDict = {0:"일의 자리",
               1:"십의 자리",
               2:"백의 자리",
               3:"천의 자리",
               4:"만의 자리"}
    print(f"숫자 : {num}")
    for i in range(len(num)):
        print(f"{numDict[(len(num) - 1) - i]} : {num[i]}")
user = input("숫자 : ")
numWhere(user)
