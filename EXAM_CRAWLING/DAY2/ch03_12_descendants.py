from	urllib.request	import	urlopen
from	bs4	import	BeautifulSoup

html	=	urlopen('http://www.pythonscraping.com/pages/page3.html')
soup	=	BeautifulSoup(html,	'html.parser')

# 자손 : descendants
desc = soup.find("table", {"id":"giftList"}).descendants
list_desc = list(desc)
print("자손 개수:", len(list_desc))

for tag in list_desc:
    print(tag
          )