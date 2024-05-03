import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
0 : 지역!
1 : 매장명!
2 : 상태
3 : 주소!
4 : 전화번호!
'''
# csv -> DF로 넘어갈 때 첫줄은 header이기 때문에 header 미리 저장
local_list = ["위치(시,구)"] # 0번
name_list = ["매장이름"] # 1번
addr_list = ["주소"] # 3번
num_list = ["전화번호"] # 4번
cnt = 1 # 매장개수
# page number 1~51
for page in range(1, 52):
    hollys = urlopen(f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store=")
    soup = BeautifulSoup(hollys, "html.parser")
    # print(page)
    for info in soup.tbody.select("tr"):
        hollys_center = list(info.stripped_strings)
        # print(hollys_center)
        local_list.append(hollys_center[0])
        name_list.append(hollys_center[1])
        addr_list.append(hollys_center[3])
        try: # 전화번호 없는 경우가 있음 혹은 .인 경우
            num_list.append(hollys_center[4])
            phone = hollys_center[4]
        except:
            phone = "."
            num_list.append(phone)

        print(f"[{cnt:3>}]: 매장이름: {hollys_center[1]}, 지역: {hollys_center[0]}, 주소: {hollys_center[3]}, 전화번호: {phone}")
        cnt+=1
        # print(f"매장{cnt}")
print(f"전체 매장 수: {cnt-1}")

with open("hollys_branches.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for row in zip(name_list, local_list, addr_list, num_list):
        # print(row)
        writer.writerow(row)

print("hollys_branches.csv 저장 완료")
