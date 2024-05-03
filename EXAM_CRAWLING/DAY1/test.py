from urllib.request	import	urlopen
html = urlopen('https://www.daangn.com/hot_articles')
print(type(html))
print(html.read())

# 크롬 창에 적힌게 title
# h1~h6는 글씨 크기