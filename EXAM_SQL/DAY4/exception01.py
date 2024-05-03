# 예외처리 1
(x, y) = (2, 0)
try:
    z = x/y
except ZeroDivisionError:
    print("0으로 나누는 예외")

try:
    z = x/y
except ZeroDivisionError as e:
    print(e)