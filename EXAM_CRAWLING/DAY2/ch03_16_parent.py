from urllib.request	import	urlopen
from bs4 import	BeautifulSoup

html	=	urlopen('http://www.pythonscraping.com/pages/page3.html')
soup	=	BeautifulSoup(html,	'html.parser')

style_tag = soup.style
print(style_tag.parent)

img1 = soup.find("img", {"src":"..img/gifts/img1.jpg"})
text = img1.parent.previous_sibling.get_text()
print(text)