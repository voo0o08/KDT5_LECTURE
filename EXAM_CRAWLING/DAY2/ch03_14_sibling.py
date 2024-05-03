'''
next_siblings : 다음 형제들
previous_siblings : 이전 형제들
'''
from urllib.request	import	urlopen
from bs4 import	BeautifulSoup

html	=	urlopen('http://www.pythonscraping.com/pages/page3.html')
soup	=	BeautifulSoup(html,	'html.parser')

sibling1 = soup.find("tr", {"id":"gift3"}).next_sibling
print("sibling1:", sibling1)
print("len(sibling1):",len(sibling1))
print(ord(sibling1))