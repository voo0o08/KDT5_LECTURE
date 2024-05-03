# list의 요소/원소 데이터 변경 및 삭제

msgList = list("Merry christmas")
print(msgList)
# ['M', 'e', 'r', 'r', 'y', ' ', 'c', 'h', 'r', 'i', 's', 't', 'm', 'a', 's']
# =>' '데이터를 '***'변경하기
msgList[5] = '***'
print(f'msgList => {msgList}')

# 삭제 => del데이터 또는 del(데이터)
del msgList[5] # ***삭제하기 del(msgList[5])해도 됨
print(f"msgList => {msgList}")