'''
12. 2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 다른 문자로 출력하는
 게임으로 아래 조건을 만족하도록 구현하자.
 - 숫자를 int형 타입으로 input함수를 이용하여 입력받는다.
 - 2, 4, 8 숫자가 있을 경우 #을 나타나게 한다.
 - 입력받은 숫자가 1000일 경우 1부터 1000 까지에 해당하는 2, 4, 8을
 #으로 출력한다.
 - 한 줄에 20개씩 출력한다.
 '''
num = int(input("게임 정수 입력 : "))
for idx, val in enumerate(range(1, num+1), 1):
    if str(val)[-1] in ("2", "4", "8"):
        print("#", end="")
    else:
        print(val, end="")
    if idx%20 == 0:
        print()