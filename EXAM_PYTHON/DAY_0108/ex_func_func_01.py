'''

'''
def print_hello():
    hello = "hello~!"

    def print_message():
        print(hello)

    print_message()

# 함수 호출
print_hello()

def a():
    x = 10

    def b():
        nonlocal x # 가장 가까운 바깥 함수에서 변수 x를 찾음
        x=20
    b()
    print(x)

a()