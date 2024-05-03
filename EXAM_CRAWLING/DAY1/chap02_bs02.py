html_example = '''
 <!DOCTYPE	html>
 <html	lang="en">
 <head>
     <meta	charset="UTF-8">
     <meta	name="viewport"	content="width=device-width,	initial-scale=1.0">
     <title>BeautifulSoup	활용</title>
 </head>
 <body>
     <h1	id="heading">Heading	1</h1>
     <p>Paragraph</p>
     <span	class="red">BeautifulSoup	Library	Examples!</span>
     <div	id="link">
         <a	class="external_link"	href="www.google.com">google</a>
         <div	id="class1">
             <p	id="first">class1's	first	paragraph</p>
             <a	class="external_link"	href="www.naver.com">naver</a>
             <p	id="second">class1's	second	paragraph</p>
             <a	class="internal_link"	href="/pages/page1.html">Page1</a>
             <p	id="third">class1's	third	paragraph</p>
         </div>
     </div>
     <div	id="text_id2">
     Example	page
     <p>g</p>
     </div>
     <h1	id="footer">Footer</h1>
 </body>
 </html>
 '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, "html.parser")

print(soup.title) # 태그까지 싹 출력
print("===============================================")
print(soup.title.string) # 태그 내부의 진짜 알맹이만 출력
print("===============================================")
print(soup.get_text())
print("===============================================")
print(soup.body)
print("=======================h1 접근========================")
print(soup.h1)


'''
a태그는 총 3개가 있음 그 중 첫번재가 출력됨
'''
print("=======================a 태그 접근========================")
print(soup.a)
print(soup.a.string)
print(soup.a['href'])
print(soup.a.get('href'))

print("=======================find() 함수 사용========================")
print(soup.find("div", {"id":"text_id2"}))
print("text사용**\n",soup.find("div", {"id":"text_id2"}).text)
print("string사용**\n",soup.find("div", {"id":"text_id2"}).string)
'''
soup은 내용을 다 담고 있기때문에 find를 이용하여 양을 줄이는 것 
string은 결과가 None이 뜸 -> text 출력을 봤을 때 두 개 이상이면 string에 None뜸
'''
print("=======================find() 함수 활용========================")
# a태그 중 class 속성 값이 internal_link인 정보 추출
href_link = soup.find("a", {"class": "internal_link"})
href_link = soup.find("a", class_="internal_link")

print(href_link)
print(href_link["href"])
print(href_link.get("href"))
print(href_link.text)

print("=======================find() 함수 활용 - attrs ========================")
print("href_link.attrs: ", href_link.attrs)
print("class 속성값: ", href_link["class"])

print("values(): ", href_link.attrs.values()) # 모든 속성들의 값 출력

values = list(href_link.attrs.values()) # 딕셔너리 값들을 리스트로 변경
print('values[0]:	{0},	values[1]:	{1}'.format(values[0],	values[1]))


print("=======================find() 함수 활용 - href 속성이 구글인 항목 검색 ========================")
href_value = soup.find(attrs={"href":"www.google.com"})
href_value = soup.find("a", attrs={"href":"www.google.com"})

print("href_value: ", href_value)
print(href_value["href"])
print(href_value.string)

print("=======================find() 함수 활용 - span 태그의 속성 가져오기 ========================")
span_tag = soup.find("span")
print("span tag:", span_tag)
print("attrs:", span_tag.attrs)
print("value:", span_tag.attrs["class"])
print("text:", span_tag.string)

print("======================= find_all() ========================")
div_tags = soup.find_all("div") # 모든 div 태그를 검색 (리스트 형태로 반환)
print("div_tags length: ", len(div_tags))

for div in div_tags:
    print('-----------------------------------------------')
    print(div)

print("======================= find_all() : 모든 a 태그 검색 및 속성 보기 ========================")
links = soup.find_all("a")
for alink in links:
    print(alink)
    print(f"url:{alink['href']}, text:{alink.string}")
    # href 무조건 작은 따옴표로 사용할 것 -> ??ㅇㅅㅇ
    print()

print("======================= find_all() : 여러 속성을 한 번에 검색 ========================")
link_tags = soup.find_all("a", {"class":["external_link", "internal_link"]})
print(link_tags)

print("======================= find_all() : 여러 속성을 한 번에 검색 ========================")
# p 태그의 id 값이 fist/third인 항목 검색
p_tags = soup.find_all("p", {"id":["first", "third"]})
for p in p_tags:
    print(p)

print("======================= select() ========================")
'''
find all과 유사함 조건에 맞는 모든 태그를 찾아 return

select_one()은 find()와 유사
'''
head = soup.select_one('head')
print(head)

print("======================= select() ========================")
# h1 태그 id가 footer 인 항목
footer = soup.select_one("h1#footer")
print(footer)

print("======================= select() ========================")
class_link	=	soup.select_one('a.internal_link')
print(class_link)


print("======================= select() ========================")
print(class_link.string)
print(class_link['href'])

print("======================= select() vs find() ========================")
link_find = soup.find('div', {'id':'link'})

external_link = link_find.find("a", {"class":"external_link"})
print("find external_link: ", external_link)


print("======================= select_one() ========================")
link2 = soup.select_one("div#class1 p#second") # [tag]#[id]
print(link2)
print(link2.string)

print("======================= select() ========================")
h1_all = soup.select("h1")
print("모든 h1 태그 검색: ", h1_all)

print("모든 url 링크 검색: ")
url_links = soup.select("a")
for link in url_links:
    print(link["href"])

print("div id=class1 내부의 모든 url 검색")
div_urls = soup.select("div#class1 > a")
print(div_urls)
print(div_urls[0]["href"])

print("div id=class1 내부의 모든 a 태그는 자손 관계")
# 공백 구분은 추천하지 않음
div_urls2	=	soup.select('div#class1	a')
print(div_urls2)

print("======================= select() - 여러 항목 검색하기 '어쩌구, 저쩌구, 웅냥냥' ========================")
print("h1 태그의 id가 heading과 footer인 것 검색")
h1 = soup.select("#heading, #footer")
print(h1)

print("a 태그의 class 이름이 external_link와 internal_link인 것 모두 검색")
url_links = soup.select("a.external_link, a.internal_link")
print(url_links)

national_anthem	=	'''
<!DOCTYPE	html>
<html	lang="en">
<head>
    <meta	charset="UTF-8">
    <title>애국가</title>
</head>
<body>
    <div>
        <p	id="title">애국가</p>
        <p	class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p	class="content">
            남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p	class="content">
            가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p	class="content">
            이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>																
    </div>
</body>
</html>
'''

soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').string)

contents = soup.select('p.content')
for content in contents:
    print(content.text)