import pandas as pd

f = "hollys_branches.csv"
hollys_df = pd.read_csv(f, encoding="utf-8", index_col="매장이름")

#print(hollys_df)
while True:
    user = input("검색할 매장의 도시를 입력하세요: ")
    # 종료조건 : 사용자의 quit 입력
    if user == "quit":
        break
    user_df = hollys_df[hollys_df["위치(시,구)"].str.contains(user)]
    print("-"*30)
    print("검색된 매장 수: ", len(user_df))
    print("-"*30)
    for idx in range(len(user_df)):
        print(f"{idx+1:3>}: {user_df.iloc[idx].values[1:]}")
    print("-"*90)



