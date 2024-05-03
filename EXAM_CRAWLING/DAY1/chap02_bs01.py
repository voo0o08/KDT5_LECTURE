from	urllib.request	import	urlopen
from	bs4	import	BeautifulSoup

# 만약 h1이 여러 개라면 제일 먼저 발견되는 거 하나만  찾음
html = urlopen("http://www.daangn.com/hot_articles")
bs = BeautifulSoup(html.read(), "html.parser")

print(bs.h1)
print(bs.h1.string.strip())
