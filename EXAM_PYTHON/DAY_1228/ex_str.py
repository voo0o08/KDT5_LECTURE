# -----------------------------------------------------
#  문자/문자열 데이터 살펴보기 => str 데이터 타입
#  -규칙/문법 => '데이터'

msg="Happy New Year 2024!"
print(msg)

# -----------------------------------------------------------
# 문자/글자 안에서 일부분만 추출해서 다루기 => 인덱싱(Indexing)
# -왼쪽 => 오른쪾 : 0, 1,

print(f'0번 원소 => {msg[0]}')
print(f'0번 원소 => {msg[19]}')
# print(f'0번 원소 => {msg[20]}') # index out of range : 인덱스 범위를 벗어나면 오류 발생
print(msg[0], msg[1], msg[2], msg[3], msg[4], sep="")
print()
# 2024!만 화면에 출력하기
print(msg[-5:])

# -----------------------------------------------------------
# 문자/글자 안에서 일부분만 추출해서 다루기 => 슬라이싱(Slicing)
# -원소/요소 추출 규칙/문법 => 변수명[시작인덱스:끝인덱스+1:간격]
# -조건 : 연속된 인덱스 또는 규칙이 있는 인덱스
print(msg[0:5]) # 0~4
print(f'msg[0:5] => {msg[0:5]}')
# Happy만 화면에 출력하기 => 슬라이싱으로 출력하기
print(msg[-5:20])
print()

# 첫번째부터 시작하는 경우 시작 인덱스 생략 가능
# 마지막까지인 경우 마지막 인덱스 생략 가능
print(f"처음부터 끝까지 출력하기 {msg[:]}")
print()

# -----------------------------------------------------------
# 연속은 아니지만 규칙이 있는 경우의 슬라이싱
# -변수명[시작:끝+1:간격/규칙]
# -----------------------------------------------------------
msg = "123456789"

# msg 안에서 2468 요소만 출력하고 싶음
print(msg[1:8:2])

# 문자열 안에서 3의 배수에 해당하는 숫자만 뽑기
print(msg[2::3])
