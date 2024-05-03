from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://blog.naver.com/swf1004/221631056531")

driver.switch_to.frame("mainFrame")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

whole_border = soup.find("div", {"id":"whole-border"})
results = whole_border.find_all("div", {"class":"se-module"})

result1 = []
for result in results:
    print(result.text.replace("\n", ""))
    result.append(result.text)