'''
25. 정수, 실수, 논리, 문자열 등 데이터 입력 시 모두 덧셈한 결과 출력하는 함수
 생성하세요.
- 입력은 함수에 포함하지 않음
- 입력 데이터 수는 미정/가변
- 입력 데이터 종류는 한번에 1개 데이터 타입
 * 정수면 정수 데이터만, 문자열이면 문자열 데이터만
2, 9, 3, 5, 8, 7
True, True, False, False, True
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
'''
# def addData(*datas):
#     print(datas)
#     if len(datas) == 1 and not(datas[0]):
#         return print("None")
#     string = ""
#     num = 0
#     for data in datas:
#         if data.isdigit():
#             num += int(data)
#         else:
#             if "True" in data:
#                 print("참")
#                 num += 1
#                 continue
#             elif "False" in data:
#                 continue
#             string += data
#
#     if string:
#         return print("문자열", string)
#     else:
#         return print("숫자", num)
#
#
# user = input("계산하고 싶은 데이터 입력 : ").split(",")
# addData(*user)