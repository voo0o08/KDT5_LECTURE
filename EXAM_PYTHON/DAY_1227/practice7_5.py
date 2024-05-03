# 81p 날짜와 시간 출력하기
year, mon, day, h, m, s = input("날짜와 시간을 입력 : ").split()
print(year, mon, day, sep="-", end="T")
print(h,m,s,sep=":")