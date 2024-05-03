### => 모듈 로딩
import cgi, sys, codecs, os

### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


### -------------- 사용자 정의 함수
def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열
    filename="./html/text.html"
    with open(file=filename, mode="r", encoding="utf-8") as f:
        ### HTML Header
        print("Content-Type: text/html; charset=utf-8")
        print() # 한 줄을 꼭 띄어야 헤더와 바디를 구분할 수 있음 
        
        ### HTML Body
        print(f.read().format(result))

### -------------- 요청 처리 및 브라우징
### => Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()

### => 데이터 추출
if "data" in form:
    result=form.getvalue("data") # 딕셔너리처럼 form["data"]로 사용 가능 
else:
    result="No Data"
    
### => 브라우징
print_browser(form)


        
        