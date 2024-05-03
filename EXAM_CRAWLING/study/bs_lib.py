from urllib.request import urlopen
from bs4 import BeautifulSoup

rating_page = urlopen("https://workey.codeit.kr/ratings/index")
print(rating_page)

soup = BeautifulSoup(rating_page, "html.parser")

program_title_tages=  soup.select("td.program")
for tag in program_title_tages:
    # print(tag.get_text()) # method
    print(tag.text) # property

print("\n======= 1위 프로그램 정보 td =======")
tags = soup.select('td')[:4]
# print(tags.text)
print(type(tags))
print("tags 길이:", len(tags))
for tag in tags:
	print(tag.text)

print("\n======= 1위 프로그램 정보 tr =======")
tags = soup.select('tr')[1]
print(type(tags))
print("tags 길이:", len(tags))
print(tags.text)
for i in range(len(tags)):
    print(i, tags[i])