'''
다양한 함수의 형태 - 특별한 함수 (2)
- 매개변수의 개수를 유동적으로 가변하는 함수
- key/value 덩어리 데이터
- 형태 : def 함수명( **data ):
- 가변 인자 함수
- 매개 변수 개수 : 0~N
- 호출: 함수명(key1=value1, key2=value2...)
'''

aDict = {"my_name":"Hong", "age":100}
aDict.update(job = "학생", birth = "1112", blood = "A")

def add(x,y):
    '''
    gg
    :param x:
    :param y:
    :return:
    '''
# doc string

'''
함수 기능 : 회원 가입 기능
함수 이름 : joinMember
매개 변수 : 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ...
          가변 + 데이터 정보 함께
          키워드 파라미터 **member
반 환 값 : '가입 완료 되었습니다.'str
'''
def joinMember(**member):

    print(member)
    # 멤버 저장소에 멤버 추가하기
    members.append(member)

# 함수 사용 = 호출
# 가입된 회원들 저장 변수
members = []
# 회원가입 기능 함수 호출
joinMember(name='hong', age = 17, birth = '2020/10/10')
joinMember(id='hong84', phone = "010-1234-5678", job = 'doctor', blood = "B")
joinMember(id='baby', birth = '2020/10/10', blood = "A")
print(members)

print()
# 딕셔너리 ver
def joinMember1(**member):

    print(member)
    # 멤버 저장소에 멤버 추가하기
    members[f'M{len(members)+1}'] = member

# 함수 사용 = 호출
# 가입된 회원들 저장 변수
members = {}
# 회원가입 기능 함수 호출
joinMember1(name='hong', age = 17, birth = '2020/10/10')
joinMember1(id='hong84', phone = "010-1234-5678", job = 'doctor', blood = "B")
joinMember1(id='baby', birth = '2020/10/10', blood = "A")
print(members)

print()
'''
회원가입2
필수 입력 항목인 ID와 PW가 필요함
option => 이름 전화번호 취미 주소 생일
'''
def joinMember2(id, pw, **option): # 필수 입력란이 앞으로 가도록 할 것 : option이 몇개가 될지 모르니꼐

    print("ok")

joinMember2("hong123", 1234)


print()
'''
회원가입3 : default 만들기
필수 입력 항목 : id pw loc gender 
option => 이름 전화번호 취미 주소 생일
'''
members = {}
def joinMember3(id, pw, loc="내국인", gender = "남자", **option):

    print("ok")
    valDict = {}
    valDict["pw"] = pw
    valDict["loc"] = loc
    valDict["gender"] = gender
    valDict["etc"] = option
    members[id] = valDict
joinMember3("hong123", 1234)
print(members)
