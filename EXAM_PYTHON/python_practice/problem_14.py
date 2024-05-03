'''
14. 숫자와 화폐단위 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요.
- 입력은 함수에 넣지 않습니다.
- 세자리 마다 쉼표와 화폐 단위를 구성해서 출력하는 사용자 정의 함수 생성
1234567, $
907, ￦
'''
def comma(moneyStr):
    num = int(moneyStr.split(",")[0])
    money = moneyStr[-1]
    print(f"{num:,}{money}")

comma(input("숫자 입력 : "))