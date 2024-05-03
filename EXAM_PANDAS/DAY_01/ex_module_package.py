'''
모듈과 패키지
- 관계:
    * 모듈 : 특정 기능/목적의 변수, 함수, 클래스를 저장한 하나의 파이썬 파일.py
    * 패키지 : 특정 기능/목적의 모듈 모음
- 문법 : import 모듈명
        improt 패키지명.모듈명
'''
# 사용할 모듈 로딩 ---------------------------------
import math # 내장 모듈, math 모듈 내 모든 변수, 함수, 클래스 다 사용
# import math as m -> math의 별칭을 m으로 지어주는 것 m.~로 사용하면 됨
# from math import factorial # -> math에서 factorial()만 가져오는 것
from math import factorial as fac #함수명 factorial의 별칭으로 fac를 사용하는 것
def fac(a, b):
    print(a+b)
print(fac(1, 3))
# 만약 해당 파일에 import한 함수와 똑같은 이름의 파일을 만든다면 내가 만든 것 우선

from math import * # math.안해도 됨
# 모듈 내의 요소(변수, 함수, 클래스) 사용 방법
# => 모듈명.변수
# => 모듈명.함수()
print(math.pi) # 모듈명.변수
print(math.pow(2, 3)) # 모듈명.함수()