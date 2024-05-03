'''
filter(함수명, 반복 가능 객체)
- 조건에 맞는(True) 데이터만 반환
'''

# 5초과 10미만 데이터만 추출
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

def check(data):
    return data>5 and data<10
print(list(filter(check, a)))

# import random -> random.py 안에 모든 변수, 함수, 클래스 가져오기
# from random import randint -> random.py 파일에서 randint 함수만 가져오기
# from random import randint, random -> random.py 파일에서 randint, random 함수만 가져오기
from functools import reduce
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

def f(x,y):
    return x+y
print(reduce(f,a))

# lambda ver
print(reduce(lambda x, y : x+y, a))