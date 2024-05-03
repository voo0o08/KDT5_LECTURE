# for 요소 in 시퀀스/반복가능한 객체:
# ==> for 인덱스 in range(len(변수)) :
# ==> 내장함수 enumerate()
# -(번호, 요소) tuple 묶음으로 반환

datas = ["apple", "banana", "Orange"]

for idx, data in enumerate(datas, 1):
    print(idx, data)

x = ['std01', 'std02', 'std03']
y = [100, 200, 300]

myDict = {}
for idx, key in enumerate(x):
    # data = (0, "std01")
    myDict[key] = y[idx]
