'''
8. 아래와 같이 출력된 함수를 구현해 주세요.
[ -2, 3, 0, 2, -5 ]
[-3, -2, -1, 0, 1, 2, 3 ]
리스트 길이는 2~3
'''
def sumZero(nums):
    sumList = [] # 모든 조합을 담은 리스트
    tempList2 = []
    tempList3 = []
    for idx1, num1 in enumerate(nums):
        tempList2.append(num1)
        for idx2, num2 in enumerate(nums[idx1:], idx1):
            if idx1 != idx2:
                tempList2.append(num2)
                tempList3 = tempList2.copy()
                tempList2 = tempList2[:-1]
                for idx3, num3 in enumerate(nums[idx2:], idx2):
                    if idx3 != idx1 and idx3 != idx2:
                        tempList3.append(num3)
                        sumList.append(tempList3.copy())
                        tempList3 = tempList3[:-1]
                tempList3.clear()
        tempList2.clear()

    resultList = []
    for list23 in sumList:
        if sum(list23) == 0:
            print(list23)
            resultList.append(list23)
    print(len(resultList))

inData = list(map(int,input("nums : ")[1:-1].split(",")))
sumZero(inData)