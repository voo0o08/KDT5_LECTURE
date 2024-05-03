# 16장/19장/22장

# #------------------------------16장------------------------------
# # 16.2.2 증가폭 사용하기
# # for 변수 in range(start, end, 증가폭)
# for i in range(0, 10, 2):
#     print("Hello World", i)
#
# # 16.2.3 숫자 감소시키기
# # for 변수 in range(start, end, 감소)
# for i in range(10, 0, -1):
#     print("Hello World", i)

# '''
# 16.5 리스트의 요소에 10을 곱해서 출력하기
# '''
# x = [49, -17, 25, 102, 8, 62, 21]
#
# for i in x:
#     print(i * 10, end=' ')

# '''
# 16.6 구구단 출력하기
# input으로 정수 입력
# 구구단 출력
# '''
# num = int(input())
# for i in range(1, 10):
#     print(f"{num} * {i} = {num*i}")

# #------------------------------19장------------------------------
# # 대각선으로 별 출력하기
# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
#
# # 19.5 역삼각형 모양으로 별 출력하기
# for i in range(5):
#     for j in range(5):
#         if i <= j:
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()

# # 19.6 산 모양으로 별 출력하기
# num = int(input())
# count = 1
# for i in range(num):
#     star = count*"*"
#     print(f"{star:^{2*num-1}}")
#     count += 2


#------------------------------22장------------------------------

# # 22.09 리스트에서 특정 요소만 뽑아내기
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
# b = [word for word in a if len(word) == 5]
# print(b)
#
# # 22.10 2의 거듭제곱 리스트 생성하기
# num1, num2 = map(int, input().split())
# pow_nums = [pow(2,i) for i in range(num1, num2+1) if num1 in range(1, 21) and num2 in range(10, 31) and num1<num2]
# del pow_nums[-2]
# del pow_nums[1]
# print(pow_nums)