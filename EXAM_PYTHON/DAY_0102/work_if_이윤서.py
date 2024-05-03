# # 13.6 if 조건문 사용하기
# x = 5
# if x != 10:
#     print("ok")
#
# # 13.7 온라인 할인 쿠폰 시스템 만들기
# '''
# 표준입력:
# 2700
# Cash3000
# '''
cash = int(input())
coupon = input()
# coupon = int(input().split("h")[1])
# print(cash-coupon)
if coupon == "Cash3000":
    print(cash-3000)
if coupon == "Cash5000":
    print(cash-5000)

#
# # 14.6 합격 여부 판단하기
# written_test = 75
# coding_test = True
#
# if written_test >= 80 and coding_test == True:
#     print('합격')
# else:
#     print('불합격')

# # 14.7 합격 여부 판단하기
# '''
# 평균이 80 이상일 때 합격
# 0~100인지 판단 : '잘못된 점수'
# 표준 입력 : 89 72 93 82
# '''
# kor, eng, math, sci = input().split() # 국어 영어 수학 과학
# kor = int(kor); eng = int(eng); math = int(math); sci = int(sci)
# if 0<=kor<=100 and 0<=eng<=100 and 0<=math<=100 and 0<=sci<=100:
#     mean = (kor+eng+math+sci)/4
#     if mean >= 80:
#         print("합격")
#     else:
#         print("불합격")
# else:
#     print("잘못된 점수")

# 15.3 if elif else 모두 사용하기
x = int(input())
if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# 15.4 교통카드 시스템 만들기
'''
표준입력 : 나이 >= 7
현재 잔액 : 9000
'''
age = int(input())
balance = 9000

if 7<=age<=12:
    balance -= 650
elif 13<=age<=18:
    balance -= 1050
else:
    balance -= 1250

print(balance)