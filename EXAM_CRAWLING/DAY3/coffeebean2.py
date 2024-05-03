from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome() # 윈도우에서는 크롬 안에 아무것도 넣으면 x
driver.get("https://www.coffeebeankorea.com/store/store.asp")

# 팝업창 생성
driver.execute_script("storePop2(1)")

# 현재의 html 소스를 저장
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

store_names = soup.select("div.store_txt > p.name > span")
store_name_list = []
for name in store_names:
    store_name_list.append(name.get_text())

print('매장 개수:	', len(store_name_list))
print(store_name_list)
store_addresses = soup.select('p.addr > span')
store_address_list = []
for addr in store_addresses:
    print(addr.get_text())
    store_address_list.append(addr.get_text())

driver.quit()  # web	driver	종료