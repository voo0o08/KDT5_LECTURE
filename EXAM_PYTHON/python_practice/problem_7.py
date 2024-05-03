'''
7. 아래와 같이 출력되는 함수를 구현해 주세요.
- 정수 리스트 안에 2가 포함된 연속된 부분 리스트를 찾아서 반환
- 정수 리스트 안에 2가 1개 포함 된 경우 [2] 반환
- 정수 리스트에 2가 없는 경우 [-1]
 [ 0, 1, 2, 4, 5, 2, 9 ]
 [ 0, 1, 2, 4, 5, 2, 9, 3, 2, 8, 1 ]
 [ 0, 1, 2, 4, 5, 3, 1, 7 ]
 [ 0, 0, 0 ]
'''
def cnt2(List):
    numList = [int(i) for i in nums if i.isdigit()]
    cnt = numList.count(2)
    if cnt == 0:
        return [-1]
    elif cnt == 1:
        return [2]
    else:
        idx1 = numList.index(2)
        idx2 = idx1
        for i in range(numList.count(2)-1):
            idx2 = numList.index(2, idx2+1)
        return numList[idx1:idx2+1]

nums = input("nums : ")
print(cnt2(nums))