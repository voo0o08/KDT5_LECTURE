from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(html, "html.parser")

print("현재 위치", soup.h2.text)
print("현재 온도", soup.select_one(".temperature_text").text[6:])
print("날씨 상태", soup.select_one(".before_slash").text)
print("공기 상태:")
state = soup.select_one(".today_chart_list").text.split()

print("미세먼지", state[1])
print("초미세먼지", state[3])
print("자외선", state[5])
print(state[6], state[7]) # 일몰일 때도 있고, 일출일 때도 있어서 걍 state[6]

print("-"*30)
print("시간대별 날씨 및 온도")
print("-"*30)

times = soup.select_one(".graph_inner._hourly_weather").text.split()
for i in range(0, len(times), 3):
    print(f"{times[i]:8}{times[i + 1]:10}{times[i + 2]}")