from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
'''
참조에 의한 호출 -> list, dict, set 
값에 의한 호출 -> str
'''

def coffeebean_store(store_list):
    coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome()

    for i in range(1,390):
        driver.get(coffeebean_url)
        time.sleep(1)

        driver.execute_script("storePop2(%d)"%i)
        time.sleep(1)
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            store_name = soup.select_one("div.store_txt>h2").text
            store_info	=	soup.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_addr = store_address_list[0] # 매장 주소
            store_phone = store_info[3].text # 매장 전화번호
            print('{}	{}	{}'.format(i + 1, store_name, store_addr, store_phone))
            store_list.append([store_name, store_addr, store_phone])
        except:
            continue

def	main():
    store_info	=	[]
    coffeebean_store(store_info) # 함수 호출 (list -> 참조에 의한 호출)
    #	DataFrame으로 변경
    coffeebean_table	=	pd.DataFrame(store_info,	columns=('매장이름',	'주소',	'전화번호'))
    print(coffeebean_table.head())
    #	DataFrame을 csv파일로 저장 (utf-8로 인코딩)
    coffeebean_table.to_csv('coffeebean_branches.csv',	encoding='utf-8',	mode='w',	index=True)

main()