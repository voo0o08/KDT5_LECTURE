'''
파일을 하나 선택 후 복사본 파일 생성 하기
- 예) message.txt => messge_copy.txt
'''
filename = "message.txt"
# 읽기
with open(filename, encoding="utf8") as f:
    msgList = f.readlines()

# 쓰기
copyfilename = "message_copy.txt"
with open(copyfilename, mode="w", encoding="utf8") as f:
    f.writelines(i+"\n" for i in msgList)

# 한번에 하는 방법!!! : 원본 파일을 읽은 후
with open(filename, encoding="utf8") as of:
    with open(copyfilename, mode="w", encoding='utf8') as nf:
        nf.write(of.read())