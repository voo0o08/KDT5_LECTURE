import requests
from bs4 import  BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
music_page = response.text

soup = BeautifulSoup(music_page, "html.parser")
# print(soup.prettify()) # 전체 html 코드

print(soup.select("ul.popular__order>li")) # 하위 태그

# ver1 get_text().strip() 사용하기
print("=========get_text().strip() 사용하기==========")
popular_artists = []
for tag in soup.select("ul.popular__order>li"):
    # print(f"'{tag.get_text()}'") # 좌우로 공백이 많이 껴있음
    popular_artists.append(tag.get_text().strip())
print(popular_artists)

# ver2 string 사용하기
print("\n=========string 사용하기==========")
popular_artists = []
for tag in soup.select("ul.popular__order>li"):
    #popular_artists.append(tag.strings) # object 어쩌구로 나옴
    #popular_artists.append(list(tag.strings)) # 공백까지 전부 그대로 들어감
    popular_artists.append(list(tag.stripped_strings)[1])
print(popular_artists)
