'''
find_all(text="검색어") / 대소문자 구분해야함 
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')
princeList = soup.find_all(string='the prince')
print(princeList)
print('the prince count:	', len(princeList))