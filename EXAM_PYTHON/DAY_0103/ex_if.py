# 조건부 표현식 ===> 1줄 조건문

# 조건 True 코드 if 조건식 else 조건 False 코드

# 홀 짝 식별 후 결과 출력 코드
num = 27
if num%2:
    print("홀")
else:
    print("짝")

print("홀") if num%2 else print("짝")

# 저장도 가능함
result = "홀수" if num%2 else "짝"

result = int("300") if "300".isdecimal() else "삼백"