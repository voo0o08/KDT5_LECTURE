'''
next_siblings : 다음 형제들
previous_siblings : 이전 형제들
'''
from urllib.request	import	urlopen
from bs4 import	BeautifulSoup

html	=	urlopen('http://www.pythonscraping.com/pages/page3.html')
soup	=	BeautifulSoup(html,	'html.parser')

# next siblings 속성
for sibling in soup.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)

# previous siblings 속성
for	sibling	in	soup.find('tr',	{'id':	'gift2'}).previous_siblings:
    print(sibling)