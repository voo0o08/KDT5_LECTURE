'''
27.  문자열 ‘Merry Christmas HaPPy New YEaR’에서 대문자는 소문자로, 소문자는 대문자
 로 변환하여 출력하는 코드를 구현하세요.
- 리스트 컴프리헨션(List Conprehesion)으로 구현하세요.
'''
msg = "Merry Christmas HaPPy New YEaR"
msg = [i.upper() if i.islower() else i.lower() for i in msg ]
result = ""
for ch in msg:
    result += ch
print(result)