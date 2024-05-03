'''
9. 아래와 같이 출력된 함수를 구현해 주세요.
- 리스트 컨프리헨션으로 구현
'''
def listConprehension(n):
    mulList = [f"{n} * {i} = {n*i:>2}" for i in range(1, 10)]
    dan = " "+str(n)+"단"+" "
    print(f"{dan:-^42}")
    for idx, i in enumerate(mulList, 1):
            print(i, end="\n" if idx%3 == 0 else "\t\t")
num = int(input("단 : "))
listConprehension(num)