'''
과제3: 네이버 증시 정보 크롤링
시가 총액 10위까지의 기업 정보를 크롤링
크롤링 항목 7개 : 종목명, 종목코드, 현재가, 전일가, 시가, 고가, 저가
'''
import os
import sys
import urllib.request
import json
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


def in_row(addr_list):
    temp_dict = {}
    cnt = 1
    for addr in addr_list:
        rank = requests.get(f"https://finance.naver.com{addr}")
        soup = BeautifulSoup(rank.text, "html.parser")
        # ========== 종목명, 종목코드, 현재가, 전일가, 시가, 고가, 저가 ==========
        result = list(soup.select_one(".rate_info").stripped_strings)
        #print(list(soup.select_one(".rate_info").stripped_strings))

        result = list(soup.select_one(".new_totalinfo>dl.blind").stripped_strings)
        # print(list(soup.select_one(".new_totalinfo>dl.blind").stripped_strings))
        info_list = []
        for info in result:
            temp_list = info.split()
            # print(temp_list)
            if temp_list[0] == "종목명":
                # print("종목명:", temp_list[1])
                print(f"[{cnt:2}] {temp_list[1]}")

                info_list.append(temp_list[1])


        temp_dict[cnt] = info_list
        cnt+=1
    return temp_dict
#
#
# market = requests.get(f"https://www.jobkorea.co.kr/Recruit/GI_Read/43949788?Oem_Code=C1&logpath=1&stext=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%82%AC%EC%9D%B4%EC%96%B8%ED%8B%B0%EC%8A%A4%ED%8A%B8&listno=4")
# soup = BeautifulSoup(market.text, "html.parser")
#
# print(soup.select("#dev-template-v2-part > div > table > tbody > tr > td:nth-child(2) > div > div > table > tbody > tr > td > p:nth-child(4) > span"))

rating_page = urlopen("https://www.work.go.kr/empInfo/empInfoSrch/detail/empDetailAuthView.do?searchInfoType=VALIDATION&callPage=detail&wantedAuthNo=K151632401150027&rtnUrl=/empInfo/empInfoSrch/list/dtlEmpSrchList.do")
# print(rating_page)

#contents > section > div > div.careers-area > div:nth-child(4) > table > tbody > tr > td

soup = BeautifulSoup(rating_page, "html.parser")
# rint(soup.prettify())

result = list(soup.select_one("#contents > section > div > div.careers-area > div:nth-child(4) > table > tbody").stripped_strings)
print(result)
