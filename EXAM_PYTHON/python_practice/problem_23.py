
'''
23. 입력받은 숫자 범위 안에서 소수(Prime Number)를 찾아서 반환하는 함수 생성하세요.
'''
def primeNum(num):
    pNums = [i for i in range(2, num+1)]
    temp = []
    for idx, n in enumerate(pNums, 0):
        if n:
            for j in range(idx, num-1, n):
                pNums[j] = False
            temp.append(n)

    print(temp)
    # print(f"1 ~ {num} 범위에서 소수 : ")

user = int(input("범위 숫자 입력 : "))
primeNum(user)