'''
반복문 - 2while 반복문
- 반복의 횟수가 정해진 경우 사용 가능함
'''
# # [요청] 사용자가 알고 싶어하는 단을 입력 받아서 해당 단의 구구단을 출력하기
#
# dan = int(input("알고싶은 단을 입력하시오 : "))
#
# i = 1
# print(f"{dan:-^9}")
# while i<10:
#     print(f"{dan:<2} * {i:<2} = {dan * i:2}")
#     i += 1
dan = 2
while dan<10:
    msg = str(dan)+"단"
    print(f"{msg:-^10}")
    num = 1
    while num<10:
        print(f"{dan:^3} * {num:^3} = {dan * num:2}")
        num += 1
    dan += 1
    
