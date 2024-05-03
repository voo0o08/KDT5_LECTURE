# # 1. 아래에 데이터를 저장하는 코드를 작성하세요.
# # 1-1번
# mail1 = "kim1234@naver.com"
# print(mail1[:7])
# # 1-2번
# domain = 'http://www.naver.com'
# print(domain[-9:])
# # 1-3번
# name = "홍길동"
# print(name[1:])
# # 1-4번
# eng = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"
# print(f"대문자 : {eng[::2]}")
# print(f"소문자 : {eng[1::2]}")
# # 1-5번
# mix = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
# print(mix[3::4])
# # 1-6번
# num = "881120-1068234"
# print(f"생년월일 : {num[:6]}\n숫자부분 : {num[7:]}")



# # 2. 숫자를 입력 받은 후 2진수, 8진수, 16진수를 출력하세요.
# num = int(input("정수 입력 : "))
# print(f"10진수 : {num}\n16진수 : {hex(num)}\n 8진수 : {oct(num)}\n 2진수 : {bin(num)}")



# # 3. 3개의 단어를 입력 받은 후 가장 큰 단어, 가장 작은 단어를 출력 하세요.
# word1 = input("단어 입력 : ")
# word2 = input("단어 입력 : ")
# word3 = input("단어 입력 : ")
# print(f"코드 값이 가장 큰 단어 : {max(word1, word2, word3)}")
# print(f"코드 값이 가장 작은 단어 : {min(word1, word2, word3)}")



# # 4. 입력 받은 단어가 메시지 안에 존재하는지 여부를 출력하세요.
# msg = "오늘은 행복한 목요일입니다."
# word = input("단어 입력 : ")
# print(f"'{word}'단어 메시지 존재 여부 : {word in msg}")


# # 5. 단어 하나를 입력 받고/코드값/16진수 값을 출력하시오
# word = input("단어 입력 : ")
# print(f"'{word}' 코드값 : {ord(word[0])} {ord(word[1])} {ord(word[2])}")
# print(f"'{word}' 16진수 코드 값 : {bin(ord(word[0]))} {bin(ord(word[1]))[2:]} {bin(ord(word[2]))[2:]}")