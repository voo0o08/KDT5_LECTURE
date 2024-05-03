'''
22. 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.
- 입력은 함수에 포함하지 않음
- 구구단 출력은 가로 방향
입력 : 2 - 4
'''
def dan99(num1, num2):
    danList = list(range(num1, num2+1))
    idx = 0 # idx의 최대 값은 len(danList)-1
    j = 0 # 1 ~ 9
    while j<10:
        if idx > len(danList)-1: # idx는 n~m
            j += 1
            if j == 10:break
            idx = 0
        if j == 0:
            print(f"--{danList[idx]}단--", end="\n" if idx == len(danList)-1 else "\t")
        else:
            print(f"{danList[idx]}*{j}={danList[idx]*j:>2}", end="\n" if idx == len(danList)-1 else "\t")
        idx += 1


n1, n2 = map(int, input("시작 구구단, 종료 구구단 입력 : ").split("-"))
dan99(n1, n2)