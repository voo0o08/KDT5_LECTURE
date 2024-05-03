# ----------------------------------------------------
# str 데이터 타입 전용 함수(method) 살펴보기
# method는 특정 데이터 타입에서만 사용 가능한 함수를 의미
# 사용방법 :
# 변수명.메서드명() ==> msg="good"
#                     msg.메서드명()
# 데이터.메서드명() ==> "Good".메서드명()
# ----------------------------------------------------
# ord <-> chr

# +89페이지 객체비교 연산자
# a = -5
# print(id(a), id(-5), a is -5)
#
# a = -6
# print(id(a), id(-6), a is -6)
# 코드에서는 True로 뜨지만 console에서는 다르다고 뜨게 됨
# ----------------------------------------------------

# str을 대문자로 변환 => upper() method
# str을 소문자로 변환 => lower() method
print("Good".upper())
print("Good".lower())
print()

# str이 모두 대문자/소문자인지 검사 후 결과 반환 => isupper(), islower()
print("Good".isupper())
print("Good".islower())
print()

# str이 0-9로 구성되어 있는지 검사 후 결과 반환() => isdecimal() 메서드
print("123542".isdecimal())
print("-123542".isdecimal()) #-는 인식 못함
print()

# str이 문자로만 구성되어 있는지 검사 후 결과 반환 => isalpha() 메서드
print("Good".isalpha())
print("안녕".isalpha()) #한글도 가능
print()

# str이 문자, 숫자로만 구성되어 있는지 검사 후 결과 반환 => isalnum()
print("Good2024".isalnum())
print()
# 시작문자 끝문자가 특정한 것인지 검사하는 함수 => startwidth(), endwidth()
print("Hello".startswith("H"))
print("people.jpg".endswith("jpg"))

# str 특정 인덱스 문자를 변경해주는 메서드 => replace()메서드
name = "Hongggggg"
# name[3] = "i"
name = name.replace("g","i",)
print(name)