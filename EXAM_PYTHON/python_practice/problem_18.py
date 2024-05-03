
'''
18. 생일을 입력 받은 후 한국 나이, 만 나이를 알려주는 함수를 생성해 주세요.
- 입력 받는 기능은 함수 안에 넣지 않음
2000.04.01
2020.12.29
'''
today = 107
userInfo = input("생년월일 입력 : ").split(".")

year = int(userInfo[0])
day = int(userInfo[1]+userInfo[2])
man = 1 if day<today else 0

print(f"당신의 한국 나이는 {2024-year+1}")
print(f"당신의 만 나이는 {2024-year+man}")