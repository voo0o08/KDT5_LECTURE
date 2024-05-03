from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.coffeebeankorea.com/store/store.asp")

# storePop2(1) 호출 : 팝업 창에 1번 매장인 학동역 DT점 나타남
driver.execute_script("storePop2(1)")
time.sleep(3)

# 함수 호출 결과 페이지를 별도로 저장 후 BeautifulSoup과 연동
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())