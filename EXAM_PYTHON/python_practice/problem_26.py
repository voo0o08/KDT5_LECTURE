
'''
26. 다이아몬드 그리기!!
6 단계
'''
maxLevel = 6
lenth = 2*maxLevel-1
startNum = 1

for i in range(maxLevel*2-1):
    star = startNum * "*"
    blank = ((lenth - startNum) // 2) * " "
    startNum = startNum+2 if i+1<6 else startNum-2
    print(blank+star)

print("Good Luck 2023")