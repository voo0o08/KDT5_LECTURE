'''
파일 입출력 => 출력 즉, 읽기(Read)
- 사용 내장 함수 : open()
- 읽기의 기본모드는 r(=rt=Read Text)
- encoding 설정 : 파일에 적용된 인코딩을 설정해야 함!!
기본 동작 : 읽고 -> 쓰고 -> 닫고
'''

# 1단계 파일 열기 : open()
file = open("message.txt", encoding="UTF-8")
print(f"file => {type(file)}, {file}\n")

# 2단계 IO작업 : read()
# 파일 내의 모든 내용을 다 읽어 옴
fileRead = file.read(5)
print(fileRead)

# 2단계 IO작업 : read(n) / defualt = -1 => 숫자 n을 넣으면 n byte를 읽어줌
fileRead = file.read(5)
print(fileRead)

# 2단계 IO 한줄 씩 읽기 : readline()
# 전체 파일을 다 보려면 반복문을 돌린다
datas = []
# while True: # 위에서 읽었던 곳부터 출력됨
#     fline = file.readline()
#     if not fline:
#         break
#     print(f"line => {type(fline)}, {fline}", end="")  # 파일 자체의 줄바꿈과 print 함수의 줄바꿈 때문에 \n\n으로 들어감
#     datas.append(fline)
# ->를 구현해둔 함수가 있음 -> readlines()
datas = file.readlines()
print()
print(datas)

# 3단계 닫기 : close()
file.close()