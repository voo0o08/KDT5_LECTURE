'''
32. 아래 조건을 만족하는 함수를 생성 후 코드를 구현해주세요.
- 주민번호 ‘oooooo-ooooooo’를 해당 형식으로 입력 받음
- 입력기능은 함수에서 빠짐
- 함수 실행 결과 띠, 별자리, 나이

011010-3234567
'''
def residentInfo(pNum):
    animals = ["원숭이", "닭", "개", "돼지", "쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양"]
    sexDict = {"1" : "남자",
           "2" : "여자",
           "3" : "남자",
           "4" : "여자"}
    b_day = int(pNum.split("-")[0][2:6])
    if 1231>=b_day>=1225 or 101<=b_day<=119:
        astro = "염소자리"
    elif b_day<=218:
        astro = "물병자리"
    elif b_day<=320:
        astro = "물고기자리"
    elif b_day<=419:
        astro = "양자리"
    elif b_day<=520:
        astro = "황소자리"
    elif b_day<=621:
        astro = "쌍둥이자리"
    elif b_day<=722:
        astro = "게자리"
    elif b_day<=822:
        astro = "사자자리"
    elif b_day<=923:
        astro = "처녀자리"
    elif b_day<=1022:
        astro = "천칭자리"
    elif b_day<=1122:
        astro = "전갈자리"
    elif b_day<=1224:
        astro = "궁수자리"
    year = int("20"+pNum[:2])
    age = 2024-year-1
    sex = sexDict[pNum.split("-")[1][0]]
    mon = pNum[2:4]
    day = pNum[4:6]
    animal = animals[year%12]
    print(f"{age}세, {sex}, {year}년 {mon}월 {day}일 {animal}띠 {astro}")

num = input("주민번호 입력(000000-0000000) : ")
residentInfo(num)
