import pandas as pd

# 버전 확인
print(pd.__version__)

# 데이터 파일 읽기 -> 상대경로로 작성해야함 ..이 한번 밖으로 나가기
filename="../DATA/deliveries.csv"

data = pd.read_csv(filename)
print(type(data))
print(data)