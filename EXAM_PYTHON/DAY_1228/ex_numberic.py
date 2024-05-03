'''
논리 연산자 => and, or, not
- 결과 : True/False
- 동작방식
    * and => A and B : A, B 모두 True일 때만 True
    * or  => A or B  : A, B 중 하나 이상 True되면 Ture
    * not => not A : 현재 상태를 A의 반대로 => False, not False => True : 토글링
'''

# no1 = 10
# no2 = 3
no1, no2 = 10, 2

# and 연산자 -------------------------------
print(no1 > no2 and no1 > 100)
print(no1 > no2 and no1 < 100 and no1 > 0)

# or 연산자 -------------------------------
print(no1 > no2 or no1 > 100)
print(no1 > no2 or no1 < 100)

# not 연산자 -------------------------------
# T->F / F->T
# F = 0 / T = 0이 아닌 모든 숫자
print(not False)
print(not 0, not 1)
print(not -3, not 0.0) # -3도 True

'''
객체 비교 연산자 => is, is not
- 결과 : True/False
'''
print(f'10 is 10 => {10 is 10}')
print(f'10 is 10.0 => {10 is 10.0}')
print(f'10 == 10 => {10 == 10.0}')