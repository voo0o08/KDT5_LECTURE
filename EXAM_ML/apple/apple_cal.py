import numpy as np
temp_list = [[1, 5, 1, 2, 2, 8, 2, 1, 3, 7, 5, 9, 2, 8, 2, 5, 4], [2, 9, 4, 8, 5, 5, 9, 7, 8, 5, 4, 3, 3, 7, 6, 2, 1], [9, 7, 3, 3, 5, 4, 9, 5, 7, 9, 1, 3, 6, 9, 6, 1, 3], [8, 1, 3, 5, 7, 4, 2, 5, 4, 1, 4, 1, 7, 5, 4, 4, 2], [4, 5, 4, 4, 7, 7, 8, 8, 5, 8, 3, 9, 4, 6, 3, 9, 6], [8, 1, 7, 8, 3, 4, 5, 5, 4, 9, 5, 9, 7, 5, 1, 6, 1], [7, 1, 6, 5, 6, 9, 5, 4, 9, 9, 8, 4, 4, 1, 4, 7, 2], [8, 5, 9, 8, 7, 2, 9, 2, 4, 5, 7, 5, 2, 2, 9, 3, 2], [1, 2, 3, 2, 1, 2, 4, 5, 7, 8, 2, 6, 1, 3, 1, 6, 1], [4, 1, 2, 4, 5, 4, 2, 3, 5, 4, 9, 1, 100, 4, 1, 3, 5]]
temp_array = np.array(temp_list)
'''
무조건 사각형!! 
10인거 부터 찾기 
세로 4 가로 4
세로 3 가로 3
세로 2 가로 2
'''
length = 3 # 몇개를 한 묶음으로 할 것인지를 설정 

# test 
# List = [1, 2, 3, 4, 5]
# for i in range(len(List)-length+1):
#     print(List[i:i+length])
#     print(sum(List[i:i + length]))

print("========================main========================")

print("temp_array의 shape", temp_array.shape) # (10, 17) = (row, col)
# 가로는 길이만큼 돌리고
# 세로 묶음
for i in range(temp_array.shape[1]): # 17
    for j in range(temp_array.shape[0]-length+1): # 10
        print(j, i)
        print(temp_array[j:j + length, i])

print("======================================================")

# 가로 묶음
for i in range(temp_array.shape[0]): # 10 행
    for j in range(temp_array.shape[1]-length+1): # 17 열
        print(i, j)
        print(temp_array[i, j:j + length])


