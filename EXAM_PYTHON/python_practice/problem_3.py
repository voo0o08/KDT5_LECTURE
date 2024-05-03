
'''
3. 아래 조건을 만족하는 코드를 작성하세요.
- 'q', 'Q' 입력 전까지 동작
- 대문자 Q 제외한 나머지 알파벳 입력 시 ♠ 출력
- 소문자 q 제외한 나머지 알파벳 입력 시 ♤ 출력
- 0 ~ 9 숫자 입력 시 숫자만큼의 ◎ 출력
'''
while True:
    inputAlpha = input("알파벳 입력 : ")
    if inputAlpha in ["q", "Q"]:
        break
    if inputAlpha.isupper():
        print("♠")
    elif inputAlpha.islower():
        print("♤")
    elif inputAlpha.isdigit():
        print("◎" * int(inputAlpha))
    else:
        print("잘못된 입력")
