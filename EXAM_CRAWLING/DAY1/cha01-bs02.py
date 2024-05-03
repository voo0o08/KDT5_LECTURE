'''
bs는 전체 HTML 코드를 다 가지고 있음
여기서 필요한 자료만 긁어서 사용
bs.h1 -> h1만 긁어 온 것
bs.title -> title만 긁어 온 것
bs는 출력 해보면 <어쩌구>로 tag들이 있음 여기서 보고 싶은 부분만 보는 것
'''

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        value = bsObj.body.find(tag)
    except AttributeError as e:
        return None
    return value

tag="h1"
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag)
if value == None:
    print(f'{tag}	could	not	be	found')
else:
    print(value)