### => 모듈 로딩
import cgi, sys, codecs, os
from joblib import load
import pandas as pd

### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


### -------------- 사용자 정의 함수
def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열
    filename="./html/index.html"
    with open(file=filename, mode="r", encoding="utf-8") as f:
        ### HTML Header
        print("Content-Type: text/html; charset=utf-8")
        print() # 한 줄을 꼭 띄어야 헤더와 바디를 구분할 수 있음 
        
        ### HTML Body
        print(f.read().format(result))
        
### --------------- 모델 불러오기 및 결과 return
def model_pred(form):
    model_file = "./cgi-bin/obesity.pkl"

    # 모델 로딩 윤떠야~!!!>< 나도 
    model = load(model_file)
    age_scaler = load("./cgi-bin/age_scaler.pkl")
    height_scaler = load("./cgi-bin/height_scaler.pkl")
    
    Age = pd.DataFrame([int(form['user_age'].value)])
    height = pd.DataFrame([int(form['user_height'].value)/100])
    my_Age = age_scaler.transform(Age)
    my_height = height_scaler.transform(height)
    
    obesity_list = [
        "Insufficient_Weight",
        "Normal_Weight",
        "Overweight_Level_I",
        "Overweight_Level_II",
        "Obesity_Type_I",
        "Obesity_Type_II",
        "Obesity_Type_III",
    ]

    # 로딩된 모델 확인
    # print(model.classes_)

    if True:
        my_data = pd.DataFrame(
            [[int(form['성별'].value),
              my_Age.item(), 
              my_height.item(), 
              int(form['가족력'].value), 
              int(form['FAVC'].value), 
              int(form['FCVC'].value), 
              int(form['NCP'].value), 
              int(form['CAEC'].value), 
              int(form['SMOKE'].value), 
              int(form['CH2O'].value), 
              int(form['SCC'].value), 
              int(form['FAF'].value), 
              int(form['TUE'].value), 
              int(form['CALC'].value), 
              int(form['MTRANS'].value[0]), 
              int(form['MTRANS'].value[1]), 
              int(form['MTRANS'].value[2]), 
              int(form['MTRANS'].value[3]), 
              int(form['MTRANS'].value[4])]]
        )

        # 입력된 정보에 해당하는 비만도 알려주기
        obesity = model.predict(my_data)

        # proba = model.predict_proba(my_data)
        # print(f"{round(max(proba[0]), 2)}% {obesity_list[obesity[0]]}입니다.")
    # return obesity_list[obesity[0]]
    return obesity_list[obesity[0]]




### -------------- 요청 처리 및 브라우징
### => Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()

# ### => 데이터 추출
# if "data" in form:
#     result=form.getvalue("data") # 딕셔너리처럼 form["data"]로 사용 가능 
# else:
#     result="No Data"
    
### => 브라우징
print_browser(model_pred(form))


        
        