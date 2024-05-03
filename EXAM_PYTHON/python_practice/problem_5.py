
'''
5. 문자열을 입력하면 코드값을 아래와 같이 출력해주는 함수를 구현해 주세요.
"가나다"
'''
def encoding(strData):
    result2 = ""
    result10 =""
    for d in strData[1:-1]:
        result2+=bin(ord(d))
        result10+=hex(ord(d))
    print(f"{strData}의 인코딩 : {result10}")
    print(f"{strData}의 인코딩 : {result2}")
data = input("data=")
encoding(data)
