def foo():
    x = 10
    def test():
        return x
    return test

x = foo() # x=test()
print(x()) # !!! 중요 현재 x 또한 함수니까 ()를 꼭 붙여줘야 호출이 돼용
print(x)