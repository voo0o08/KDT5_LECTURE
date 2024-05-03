'''
타입 캐스팅(Type Casting) / 형변환
다른 데이터 타입으로 변환하는 것
int()
float()
str()
bool()
'''

# int 데이터 타입으로 형변환
# int(데이터)
print(type(int('200')))
# print(type(int('200D')))
# float->int : 소수점 이하 데이터 손실 발생
print(type(int(200.4)))
print(int(200.4))

# bool -> int
# 0과 1만 알아
print(type(int(False)), int(False))

# float 데이터 타입으로 형 변환
print(type(float('3.5')), float('3.5'))
print(type(float('3')), float('3'))
print(type(float('-3')), float('-3'))
