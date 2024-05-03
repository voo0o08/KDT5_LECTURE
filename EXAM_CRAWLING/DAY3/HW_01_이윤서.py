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

            elif temp_list[0] == "종목코드":
                #print("종목코드:", temp_list[1])
                info_list.append(temp_list[1])
            elif temp_list[0] == "현재가":
                #print("현재가:", temp_list[1])
                info_list.append(temp_list[1])
            elif temp_list[0] == "전일가":
                #print("전일가:", temp_list[1])
                info_list.append(temp_list[1])
            elif temp_list[0] == "시가":
                #print("시가:", temp_list[1])
                info_list.append(temp_list[1])
            elif temp_list[0] == "고가":
                #print("고가:", temp_list[1])
                info_list.append(temp_list[1])
            elif temp_list[0] == "저가":
                #print("저가:", temp_list[1])
                info_list.append(temp_list[1])
                break

        temp_dict[cnt] = info_list
        cnt+=1
    return temp_dict

URL_list = []
market = requests.get(f"https://finance.naver.com/sise/sise_market_sum.naver")
soup = BeautifulSoup(market.text, "html.parser")
# print(page)
for row in soup.tbody.select("tr"):
    # print(len(row))
    if len(row) != 1:
        row_data = list(row.stripped_strings)

        if int(row_data[0]) in range(1, 11):
            #print(row.select_one("a")["href"])
            URL_list.append(row.select_one("a")["href"])
            #print(row.select_one("a"))

print("------------------------------")
print("[네이버 코스피 상위 10대 기업 목록]")
print("------------------------------")
info_dict = in_row(URL_list)
name_list = ["종목명: ", "종목코드: ", "현재가: ", "전일가: ","시가: ","고가: ", "전가: "]

while True:
    user = int(input("주가를 검색할 기업의 번호를 입력하세요(-1: 종료): "))
    if user == -1:
        print("프로그램 종료")
        break

    if user not in range(1, 11):
        print("입력 에러")
        continue

    # 출력
    print(URL_list[user-1]) # URL
    for idx, val in enumerate(info_dict[user]):
        print(name_list[idx],val) # 종목명: / 값 ...


