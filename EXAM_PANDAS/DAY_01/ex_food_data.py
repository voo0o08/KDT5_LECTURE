'''
파이썬 미니 프로젝트에 파일 입출력을 이용하자
- 분류의 기준이 되는 표시가 있어야함
'''

file = "food.txt"

kor_food, china_food = [], []
kind = []

with open(file, mode='r', encoding="utf8") as f:
    data = f.readline()
    if not data.index("*"): #
        kind = "한식" if data[1:] == "한식" else "중식"
    else:
        if kind == "한식": kor_food.append(data)
        else:
            china_food.append(data)

# +딕셔너리로 해도 됨

# 기타등등
datas = ["*한식", "떡볶이", "불고기"]
# write lines로 냅다 담고 ㄲ find는 없어도 그만 있어도 그만, index는 없으면 에러남