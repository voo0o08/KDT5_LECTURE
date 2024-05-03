'''
- 익명 함수라고도 함
- 짧은 코드의 함수 또는 반복해서 재사용이 많지 않은 코드의 경우 표현
- 문법 : lambda 매개변수1, 매개변수2 ... 매개변수n : 표현식
- 결과 : 매개변수를 활용한 표현식 결과 값이 lambda 그 위치에 반환됨
'''

def add(a, b):
    return a+b
print(add(4, 5))

# 같은 표현
myAdd = lambda a, b:a+b
print(myAdd(4, 5))