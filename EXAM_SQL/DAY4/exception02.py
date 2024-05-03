# 중요!!
while True:
    try:
        n = int(input("숫자 입력 : "))
        break
    except ValueError as e:
        print(f"정수가 아닙니다. 다시 입력하시오. : {e}")
print("정수입력 완료")