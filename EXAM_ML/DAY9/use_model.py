from joblib import load

model_file = "../model/iris_dt.pkl"

# 모델 로딩
model = load(model_file)

# 로딩된 모델 확인
print(model.classes_)

# 붓꽃 정보 입력 => 4개 피쳐
datas = input("붓꽃 정보 입력(예: 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비) 입력 : ")
if len(datas):
    # data_list = datas.split(",")

    # d = datas.split(",")
    ret = list(map(float, datas.split(",")))
    print(ret)

    # 입력된 정보에 해당하는 품종 알려주기
    pre_iris = model.predict([ret])
    proba = model.predict_proba([ret])
    print(f"해당 꽃은 {proba}% {pre_iris}입니다.")
else:
    print("입력된 정보가 없습니다.")