'''
파일 입출력 => 출력=쓰기
- 사용 내장 함수 : open(file, mode = "w", encoding = 어쩌구)
- 모드 a는 append 막줄에 추가
mode 기본 값이 r이기 때문에 쓰기할 떄는 지정해줘야함
'''
filename = "mydata.txt" # 없는 파일
existfile = 'message.txt' # 있는 파일

# 1단계 onen() -> 만약 파일이 없다면 파일을 생성하고, 있다면 모든 내용을 지운다.
file = open(filename, mode="w", encoding="utf8")

# 2단계 write()
file.write("123456\n")
file.write("HaHaHa")
file.write('''
아아
''')

# 2단계 writelines() : 쓰고 싶은 거 있으면 리스트로 넣어라 물론 줄바꿈은 니 알아서 해라
file.writelines(i+"\n" for i in ["A", "B", "C"])

# 3단계 close()
