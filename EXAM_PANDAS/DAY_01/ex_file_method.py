'''
파일 데이터 접근 관련 메서드들
'''
filename = "message.txt"

with open(filename, mode="r", encoding="utf8") as f:
    f.seek(5) # 한글(3byte)로 구성되어있다면 3단위로 끊어야함 영어는 1byte라서 괜찮음!
    print(f.read(10))
    print(f"현재 위치 : {f.tell()}")

    f.seek(0)
    print(f.read(5))
    print(f"현재 위치 : {f.tell()}")

print(f.name, f.closed)