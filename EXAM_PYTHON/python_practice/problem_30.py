'''
30. 생년월일을 입력 받아 별자리를 출력해주는 기능을 구현하세요.
011010-3234567
'''
b_day = int(input("주민번호 입력(000000-0000000) : ").split("-")[0][2:6])
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

print(astro)