# ------------------------------------------------------
# str 데이터에서 특별한 의미를 가지는 문자 = 이스케이프 문자
# \문자 1개
# 외울 것

# \n : 줄바꿈
# \t : 탭간격
# \' \": 인용
# \u : unicode
# \\ : 경로 탐색, 웹 주소

# 인용부호 살펴보기
print("Happy New \"Year\" 2024~")

# 파일 경로 --------------------------------------------------
print("C:\\Users\\kdp")
# 귀찮음 방지를 위해 이스케이프 문자를 비활성화 시킬 수 있음
# r = raw data라는 의미
print(r"C:\Users\kdp")