# 임의의 숫자 데이터 7개를 저장한 리스트를 생성
# 리스트에 원소를 하나씩 화면에 출력하세요.
nums = [8, 4, 56, 6, 64, 12, 34]
print(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], sep="\n")
print()

# 아래 리스트에서 원소를 화면에 한 줄에 한개씩 출력하세요.
datas = [[10, 20], [40, 50], [70, 80, 90]]
print(datas[0][0], datas[0][1], datas[1][0], datas[1][1], datas[2][0], datas[2][1], datas[2][2], sep="\n")
print()

# 좋아하는 계절과 월을 입력받은 후 각각 변수에 저장하세요
season, month = input("좋아하는 계절과 월 입력 : ").split()
print()

# 1-20으로 구성된 정수 리스트를 생성하세요.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(f"3의 배수 인덱스에 해당하는 정수만 출력 : {my_list.index(3)}, {my_list.index(6)}, {my_list.index(9)}, {my_list.index(12)}, {my_list.index(15)}, {my_list.index(18)}")
print(f"3의 배수 인덱스에 해당하는 정수만 출력 : {my_list[3::3]}")
print(f"3의 배수 인덱스에 해당하는 정수의 합계 출력 : {my_list[3]+my_list[6]+my_list[9]+my_list[12]+my_list[15]+my_list[18]}")
