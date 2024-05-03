# ----------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => index()
# 왼쪽에서 오른쪽으로 찾기 떄문에 제일 먼저 발견되는 문자의 인덱스를 반환
data = "Merry Christmas"
print(f"data.index('C') => {data.index('C')}")
print(f"data.index('r') => {data.index('r')}")
print(f"data.index('r') => {data.index('r', 4)}") # 4번부터 r을 보겠다
# 너무 하드코딩이니 아래 처럼하자
# 처음 찾은 인덱스+1을 하면 그 다음 r을 또 찾을 수 있음
print(f"data.index('r') => {data.index('r',data.index('r')+1)}")

# !의 인덱스를 찾기
# print(f"data.index('!') => {data.index('!')}")
# - 존재하지 않는 str 인덱스를 찾으려고 하면 오류발생
# 오류가 안뜨게 하려면
print(f"data.index('!') => {data.find('!')}")
# index가 없으면 -1을 return해줌

# -------------------------------------------
# str 데이터에서 문자열 분리해주는 메서드 => split() 메서드
# - 기본값 : 스페이스 바, 공백 기준으로 1개의 str을여러 개의 str로 분리
# 반환값 : 여러 개의 str을 담아서 List로 반환
# -------------------------------------------
data = "Happy New Year"

# str에서 공백을 기준으로 str 나누기
datas = data.split()
print(type(datas))

# list에 저장된 원소/요소 하나씩 읽기 => 변수명[인덱스]
jumin_num = '123456-7894561'
birth = jumin_num[:jumin_num.index('-')]
number = jumin_num[jumin_num.index('-')+1:]
# 혹은
jumin_nums = jumin_num.split('-') # 분리 완료