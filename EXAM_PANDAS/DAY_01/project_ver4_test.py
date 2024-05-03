'''
파일 입출력 test
cur이랑 finCard int형 str로 바꾸기
1. 입력 -> a
2. 삭제 -> w (일반 덮어쓰기)
'''

userDict = {"Lee" : {"ans" : ('🦊', '🐳', '🐻', '🦊', '🐻', '🐥', '🐳', '🐳', '🐥', '🐻', '🦊', '🐥'),
                     "cur" : ('🃏', '🃏', 3, '🃏', 5, '🃏', '🃏', '🃏', '🃏', '🃏', '🃏', '🃏'),
                     "finCard" : (1, 2, 4, 6, 7, 8, 9, 10, 11, 12)},
            "Son": {"ans": ('🦊', '🐳', '🐻', '🦊', '🐻', '🐥', '🐳', '🐳', '🐥', '🐻', '🦊', '🐥'),
                    "cur": ('🃏', '🃏', 6, '🃏', 1, '🃏', '🃏', '🃏', '🃏', '🃏', '🃏', '🃏'),
                    "finCard": (1, 2, 4, 6, 7, 8, 9, 10, 11, 12)}
            }
# b = ('🦊', '🐳', '🐻', '🦊', '🐻', '🐥', '🐳', '🐳', '🐥', '🐻', '🦊', '🐥')
# a = str(userDict["Lee"]["cur"])
# print(" ".join(userDict["Lee"]["cur"]))
# print(" ".join(b))
# {이름 : {ans : cardMap, cur : userMap, finCard : finishCard}}
# {이름 : nowUserDict}

filename = "userGameLog.txt"

# 일단 처음에는 저장을 해보자!! -> 삭제 후 덮어 쓰기 용
# with open(filename, mode="w", encoding="utf8") as f:
#     for nameInput, nowUserDict in userDict.items():
#         f.writelines(nameInput+"\n")
#         f.writelines(" ".join(nowUserDict["ans"])+"\n")
#         f.writelines(" ".join(map(str, nowUserDict["cur"]))+"\n")
#         f.writelines(" ".join(map(str, nowUserDict["finCard"]))+"\n")


userDict2 = {}
# 파일을 읽어서 저장해보자!!
# {이름 : {ans : cardMap, cur : userMap, finCard : finishCard}}
with open(filename, mode="r", encoding="utf8") as f:
        userList = f.readlines()
        print(userList)
        for i in range(0, len(userList), 4):
            tempDict = {"ans" : tuple(userList[i+1][:-1].split()),
                        "cur" : tuple(int(e) if e.isdecimal() else e for e in userList[i+2][:-1].split(" ")),
                        "finCard" : tuple(int(e) if e.isdecimal() else e for e in userList[i+3][:-1].split(" "))}
            userDict2[userList[i][:-1]] = tempDict

print(userDict2)
