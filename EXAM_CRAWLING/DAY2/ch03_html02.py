from urllib.request	import urlopen
from bs4 import	BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html,	"html.parser")
#	등장인물의 이름:	녹색
nameList =	soup.find_all('span',	{'class':	'green'})
for	name in	nameList:
    print(name.string)

print("="*50)

'''
밑에 처럼하면 파일처럼 사용하는게 아닌가 싶기도??
'''
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html,	"html.parser")
#	등장인물의 이름:	녹색

while True:
    green_text = soup.find('span', {'class': 'green'})
    if green_text == None:
        break
    print(green_text)
