'''
11. 업-다운 빙고 게임 기능의 함수를 구현하세요.
- 컴퓨터에서 1 ~ 100 범위에서 임의의 수 하나 선정
- 사용자 입력 숫자와 선정된 수가 동일하면 입력 받기 중단
- 사용자 입력 숫자가 선정 수보다 큰 수인지 작은 수인지 힌트 출력
'''
import random
def upDown():
    ans = random.randint(1,100)
    print("정답은",ans)
    while True:
        user = int(input("빙고 넘버 : "))
        if user == ans:
            print("정답 - *~ 빙고 ~*")
            break
        elif user < ans:
            print(f"힌트 - {user}보다 큰 수")
        else:
            print(f"힌트 - {user}보다 작은 수")

upDown()