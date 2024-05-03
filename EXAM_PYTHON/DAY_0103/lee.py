num = int(input())
lenth = 2*num-1
count = 1
for i in range(num):
    blank = (lenth - count)//2*" "
    star = count*"*"
    count += 2
    print(blank + star)