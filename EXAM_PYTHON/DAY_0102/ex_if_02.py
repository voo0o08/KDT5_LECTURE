'''
실습1
좋아하는 정수를 하나 저장 한 후 짝수면 "짝수입니다"
홀수면 "홀수입니다"
'''

my_num = 71
if my_num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

if my_num % 2:
    print("홀수.")
else:
    print("짝수")

'''
[실습2]
# 좋아하는 정수를 하나 저장 한 후 양수면 "~는 양수입니다"
'''
if my_num>0:
    print("양수입니다")
elif my_num<0:
    print("음수입니다")
else:
    print("0")

if my_num == 0:
    print(f'{my_num} 0')
else:
    if my_num>0: # 중첩 조건문
        print("양수")
    else:
        print("음수")