'''
1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
 출력하는 함수를 구현하세요.
['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']
'''
# def min_max_str(words):
#     words.sort(reverse=True)
#     print(f"정렬 결과 : {words}")
#     print(f"가장 높은 문자열 : {words[0]}, 가장 낮은 문자열 : {words[-1]}")
# strList = input("msg=")[2:-2].split("', '")
# # print(strList)
# min_max_str(strList)
# a = ['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']

'''
2. 키보드로 입력 받은 데이터 중에서 숫자만 모두 저장하여 합계, 최대값, 최소값을
 출력하는 함수를 구현하세요.
하늘 Apple 2021 -9 False 23 7 None 끝
A 홍길동 False True True None Good Luck 가나다라
'''
# datas = input("데이터 입력 : ").split()
# numList = []
# for data in datas:
#     if not (data.isalpha()):
#         numList.append(data)
# numList = [int(num) for num in numList]
# if not(len(numList)):
#     numList.append(0)
# print(f"합계 : {sum(numList)} 최댓값 : {max(numList)} 최솟값 : {min(numList)}")

'''
3. 아래 조건을 만족하는 코드를 작성하세요.
- 'q', 'Q' 입력 전까지 동작
- 대문자 Q 제외한 나머지 알파벳 입력 시 ♠ 출력
- 소문자 q 제외한 나머지 알파벳 입력 시 ♤ 출력
- 0 ~ 9 숫자 입력 시 숫자만큼의 ◎ 출력
'''
# while True:
#     inputAlpha = input("알파벳 입력 : ")
#     if inputAlpha in ["q", "Q"]:
#         break
#     if inputAlpha.isupper():
#         print("♠")
#     elif inputAlpha.islower():
#         print("♤")
#     elif inputAlpha.isdigit():
#         print("◎" * int(inputAlpha))
#     else:
#         print("잘못된 입력")

'''
4. 아래 조건을 만족하는 코드를 작성하세요.
- 수의 범위 : 1 ~ 100
- 3의 배수 숫자 
- 7의 배수 숫자
- 8의 배수 숫자
- 3, 7, 8의 배수 숫자로 구성된 숫자만 출력
- 단!! 중복된 숫자는 제거 하세요
'''
# numList = list(range(1, 101))
# result = []
# for num in [3, 7, 8]:
#     for i in range(num-1, 101, num):
#         result.append(numList[i])
# print(set(result))

'''
5. 문자열을 입력하면 코드값을 아래와 같이 출력해주는 함수를 구현해 주세요.
"가나다"
'''
# def encoding(strData):
#     result2 = ""
#     result10 =""
#     for d in strData[1:-1]:
#         result2+=bin(ord(d))
#         result10+=hex(ord(d))
#     print(f"{strData}의 인코딩 : {result10}")
#     print(f"{strData}의 인코딩 : {result2}")
# data = input("data=")
# encoding(data)

'''
6. 문자열 리스트와 정수 1개를 입력하면 아래와 같이 출력하는 함수를 구현해 주세요.
['askde', 'beach', 'surf'] n=2
['home','pitch','python'] n=1
'''
# def sortWord(datas):
#     n = int(datas[-1])
#     words = []
#     temp = ""
#     for i in datas:
#         if i.isalpha():
#             temp += i
#         else:
#             words.append(temp)
#             temp = ""
#     result = [] # 입력에서 단어만 뽑아낸 리스트
#     for idx, w in enumerate(words):
#         if len(w) > n:
#             result.append(words[idx])
#     print("n번째로 정렬 안한 상태", result)
#
#     words_dict = {} # key = n번째 요소 / value = 해당 단어
#     for word in result:
#         words_dict[word[n]] = word
#     # print(words_dict)
#     nList = sorted(list(words_dict.keys())) # n번째 알파벳들끼리 정렬
#     # print(nList)
#
#     result2 = []
#     for nAlpha in nList:
#         result2.append(words_dict[nAlpha])
#     print(result2)
#
# datas = input("datas : ")
# sortWord(datas)

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
# def cnt2(List):
#     numList = [int(i) for i in nums if i.isdigit()]
#     cnt = numList.count(2)
#     if cnt == 0:
#         return [-1]
#     elif cnt == 1:
#         return [2]
#     else:
#         idx1 = numList.index(2)
#         idx2 = idx1
#         for i in range(numList.count(2)-1):
#             idx2 = numList.index(2, idx2+1)
#         return numList[idx1:idx2+1]
#
# nums = input("nums : ")
# print(cnt2(nums))













'''
15. 입력받은 숫자 월(Month)에 대한 영어와 한국어 표기를 출력하는 함수를 구현하세요
'''










'''
18. 생일을 입력 받은 후 한국 나이, 만 나이를 알려주는 함수를 생성해 주세요. 
- 입력 받는 기능은 함수 안에 넣지 않음
2000.04.01
2020.12.29
'''
# today = 107
# userInfo = input("생년월일 입력 : ").split(".")
#
# year = int(userInfo[0])
# day = int(userInfo[1]+userInfo[2])
# man = 1 if day<today else 0
#
# print(f"당신의 한국 나이는 {2024-year+1}")
# print(f"당신의 만 나이는 {2024-year+man}")

'''
19. 팩토리얼(Factorial)을 while반복문으로 구현해 주세요. 
 팩토리얼 수를 입력 받아서 팩토리얼 결과를 아래와 같이 출력하세요.
'''
# num = int(input("팩토리얼 수 입력 : "))
# msg = f"{num}! => "
# result = 1
#
# while num:
#     result *= num
#     msg += f"{num} =" if num == 1 else f"{num} * "
#     num -= 1
# print(msg, result)



'''
21. 아래 데이터를 저장합니다. 그리고 과목별 최고점수, 최저점수 출력하세요.
'''
# scoreDict = {"국어" : {"베트맨" : 90, "마징가" : 82, "슈퍼맨" : 77, "슈렉" : 94, "피오나" : 78},
#              "수학" : {"베트맨" : 89, "마징가" : 71, "슈퍼맨" : 100, "슈렉" : 82, "피오나" : 99},
#              "윤리" : {"베트맨" : 98, "마징가" : 80, "슈퍼맨" : 92, "슈렉" : 93, "피오나" : 91},
#              "국사" : {"베트맨" : 99, "마징가" : 91, "슈퍼맨" : 90, "슈렉" : 71, "피오나" : 83}}
# for sub, students in scoreDict.items():
#     print(f"[{sub}] 최고 점수 : {max(students.values())}, 최저 점수 : {min(students.values())}")

'''
22. 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.
- 입력은 함수에 포함하지 않음
- 구구단 출력은 가로 방향
입력 : 2 - 4
'''
# def dan99(num1, num2):
#     danList = list(range(num1, num2+1))
#     idx = 0 # idx의 최대 값은 len(danList)-1
#     j = 0 # 1 ~ 9
#     while j<10:
#         if idx > len(danList)-1: # idx는 n~m
#             j += 1
#             if j == 10:break
#             idx = 0
#         if j == 0:
#             print(f"--{danList[idx]}단--", end="\n" if idx == len(danList)-1 else "\t")
#         else:
#             print(f"{danList[idx]}*{j}={danList[idx]*j:>2}", end="\n" if idx == len(danList)-1 else "\t")
#         idx += 1
#
#
# n1, n2 = map(int, input("시작 구구단, 종료 구구단 입력 : ").split("-"))
# dan99(n1, n2)




'''
23. 입력받은 숫자 범위 안에서 소수(Prime Number)를 찾아서 반환하는 함수 생성하세요.
'''
# def primeNum(num):
#     pNums = [i for i in range(2, num+1)]
#     temp = []
#     for idx, n in enumerate(pNums, 0):
#         if n:
#             for j in range(idx, num-1, n):
#                 pNums[j] = False
#             temp.append(n)
#
#     print(temp)
#     # print(f"1 ~ {num} 범위에서 소수 : ")
#
# user = int(input("범위 숫자 입력 : "))
# primeNum(user)


'''
24. 입력받은 숫자에서 천자리, 백자리, 십자리, 일자리를 출력하세요.
- 입력은 함수에 포함하지 않음
- 숫자에서 자리 수를 출력하는 함수 구현
'''
# def numWhere(num):
#     numDict = {0:"일의 자리",
#                1:"십의 자리",
#                2:"백의 자리",
#                3:"천의 자리",
#                4:"만의 자리"}
#     print(f"숫자 : {num}")
#     for i in range(len(num)):
#         print(f"{numDict[(len(num) - 1) - i]} : {num[i]}")
# user = input("숫자 : ")
# numWhere(user)

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


'''
26. 다이아몬드 그리기!!
6 단계
'''
# maxLevel = 6
# lenth = 2*maxLevel-1
# startNum = 1
#
# for i in range(maxLevel*2-1):
#     star = startNum * "*"
#     blank = ((lenth - startNum) // 2) * " "
#     startNum = startNum+2 if i+1<6 else startNum-2
#     print(blank+star)
#
# print("Good Luck 2023")



'''
27.  문자열 ‘Merry Christmas HaPPy New YEaR’에서 대문자는 소문자로, 소문자는 대문자
 로 변환하여 출력하는 코드를 구현하세요.
- 리스트 컴프리헨션(List Conprehesion)으로 구현하세요.
'''
# msg = "Merry Christmas HaPPy New YEaR"
# msg = [i.upper() if i.islower() else i.lower() for i in msg ]
# result = ""
# for ch in msg:
#     result += ch
# print(result)

'''
28. 6가지 연산 결과를 한꺼번에 반환하는 함수를 생성 후 호출하여 결과를 아래와 같이
 출력해 주세요.
- 6가지 연산 : 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지값, 몫
'''
# def calc():
#     num1, num2 = map(int, input("숫자 2개 입력 (3, 4) : ").split(","))
#     print(f"덧셈 결과 : {num1+num2}")
#     print(f"뺄셈 결과 : {num1-num2}")
#     print(f"곱셈 결과 : {num1*num2}")
#     print(f"나누기 결과 : {num1/num2 if num2 else 0}")
#     print(f"몫 결과 : {num1//num2 if num2 else 0}")
#     print(f"나머지 결과 : {num1%num2 if num2 else 0}")
# calc()

'''
29. 다양한 사람들로부터 개인정보를 입력받는 함수를 구현하세요.
- 입력되는 개인정보의 개수는 미정
- 입력하는 사람마나 입력 데이터는 

age - 12세 id - mm1004 name - 마징가 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
'''
# def info(userInfo):
#
#     print()
#
# user = input("개인정보 : ")
# info(user)

'''
30. 생년월일을 입력 받아 별자리를 출력해주는 기능을 구현하세요.
011010-3234567
'''
# b_day = int(input("주민번호 입력(000000-0000000) : ").split("-")[0][2:6])
# if 1231>=b_day>=1225 or 101<=b_day<=119:
#     astro = "염소자리"
# elif b_day<=218:
#     astro = "물병자리"
# elif b_day<=320:
#     astro = "물고기자리"
# elif b_day<=419:
#     astro = "양자리"
# elif b_day<=520:
#     astro = "황소자리"
# elif b_day<=621:
#     astro = "쌍둥이자리"
# elif b_day<=722:
#     astro = "게자리"
# elif b_day<=822:
#     astro = "사자자리"
# elif b_day<=923:
#     astro = "처녀자리"
# elif b_day<=1022:
#     astro = "천칭자리"
# elif b_day<=1122:
#     astro = "전갈자리"
# elif b_day<=1224:
#     astro = "궁수자리"
#
# print(astro)


'''
31. 입력된 년도가 윤년인지 평년인지 평가하는 코드를 구현하세요.
'''
# def leapYear():
#     year = int(input("년도 입력 : "))
#     if year % 4 ==0 and year % 100 == 0:
#         result = "평년"
#     elif not(year % 400) or not(year % 4):
#         result = "윤년"
#     print(f"{year}년은 {result}입니다.")
# leapYear()


'''
32. 아래 조건을 만족하는 함수를 생성 후 코드를 구현해주세요.
- 주민번호 ‘oooooo-ooooooo’를 해당 형식으로 입력 받음
- 입력기능은 함수에서 빠짐
- 함수 실행 결과 띠, 별자리, 나이 

011010-3234567
'''
# def residentInfo(pNum):
#     animals = ["원숭이", "닭", "개", "돼지", "쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양"]
#     sexDict = {"1" : "남자",
#            "2" : "여자",
#            "3" : "남자",
#            "4" : "여자"}
#     b_day = int(pNum.split("-")[0][2:6])
#     if 1231>=b_day>=1225 or 101<=b_day<=119:
#         astro = "염소자리"
#     elif b_day<=218:
#         astro = "물병자리"
#     elif b_day<=320:
#         astro = "물고기자리"
#     elif b_day<=419:
#         astro = "양자리"
#     elif b_day<=520:
#         astro = "황소자리"
#     elif b_day<=621:
#         astro = "쌍둥이자리"
#     elif b_day<=722:
#         astro = "게자리"
#     elif b_day<=822:
#         astro = "사자자리"
#     elif b_day<=923:
#         astro = "처녀자리"
#     elif b_day<=1022:
#         astro = "천칭자리"
#     elif b_day<=1122:
#         astro = "전갈자리"
#     elif b_day<=1224:
#         astro = "궁수자리"
#     year = int("20"+pNum[:2])
#     age = 2024-year-1
#     sex = sexDict[pNum.split("-")[1][0]]
#     mon = pNum[2:4]
#     day = pNum[4:6]
#     animal = animals[year%12]
#     print(f"{age}세, {sex}, {year}년 {mon}월 {day}일 {animal}띠 {astro}")
#
# num = input("주민번호 입력(000000-0000000) : ")
# residentInfo(num)


