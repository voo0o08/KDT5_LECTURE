'''
다양한 함수의 형태 - (2) 반환값 없는 함수
return은 필수가 아니다!!!!
함수 기능 : 2개의 숫자를 덧셈 후 출력 해주는 기능
함수 이름 : addTwo
매개 변수 : x, y
반 환 값 : 없음
'''
def addTwo(x, y = 1):
    val = x + y
    print(f"{x} + {y} = {val}")

# 함수 사용 = 호출
addTwo(10)

'''
함수 기능 : 영어 단어를 입력 받아서 모두 대문자로 변환해주는 기능
함수 이름 : convertCase
매개 변수 : word
반 환 값 : 없음
'''
def convertCase(word):
    print(word.upper())
convertCase("hi")

'''
함수 기능 : 시퀀스 객체의 모든 원소를 모두 대문자로 변환해주는 기능
함수 이름 : convertCase2
매개 변수 : str 타입의 원소로 구성된 list
반 환 값 : 없음
'''
def convertCase2(str_list):
    for i in range(len(str_list)):
        str_list[i] = str_list[i].upper()
    print(str_list)

def convertCase3(str_list):
    for idx, i in enumerate(str_list):
        str_list[idx] = str_list[idx].upper()
    print(str_list)

convertCase2(["h", "i", "hello"])
convertCase3(["h", "i", "hello"])

# 함수 사용 즉, 함수 호출 --------------------------------------
datas = ['apple', 'banana', 'mango']
print(f"[BF] {datas}")
convertCase2(datas)
print(f"[AF] {datas}")
# 반환값이 없으면 아무 일도 안하게 됨!! return 필요할 때는 꼭 하기

