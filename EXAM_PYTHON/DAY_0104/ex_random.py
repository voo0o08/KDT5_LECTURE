# 모듈 : 특정 목적의 변수, 함수, 클래스를 하나의 파일에 담은 것
# - 예 : 수학관련 변수, 함수, 클래스 => math.py
#       파이썬 기본 제공 변수, 함수, 클래스 => builtin.py
# - 사용법 : import 모듈명
# - 모듈의 기능 사용법 : 모듈명.변수명
#                      모듈명.함수명()

import random  # 임의의 수를 추출 해주는 기능의 모듈
import math    # 수학 관련 변수, 함수, 클래스 있는 모듈

# 모듈 안에 있는 변수, 함수, 클래스 사용

print(math.pi)

print(math.factorial(5))

for cnt in range(10):
    print(random.random()) # [0~1) 사이의 임의의 실수 추출 => random() 함수

# [a~b] 사이의 임의의 정수 추출 => randint() 함수
for cnt in range(10):
    print(random.randint(1, 6))

#
myLotto = []
END_POINT = 6
print()
while True:
    if len(myLotto) == END_POINT: break
    num = random.randint(1, 45)
    if num not in myLotto:
        myLotto.append(num)
print(myLotto)

myLotto = set()
while len(myLotto) < 6:
    myLotto.add(random.randint(1, 45))
print(myLotto)
# for cnt in range(10):
#     print(random.)
