### 

## 모듈 로딩
from flask import Flask, render_template, url_for

## Application Fatory 기반의 함수 정의
## 함수명 : create_app 변경 불가
def create_app():
    ## Flask Server 인스턴스 생성
    app = Flask(__name__)
    
    ## Blueprint 인스턴스 등록 : 서브 카테고리의 페이지 라우팅
    # app.register_blueprint()
    @app.route("/")
    def index():
        return render_template('index.html')
    
    # Blueprint 인스턴스 등록 : 서브 카테고리의 페이지 라우팅 기능 
    from flask import Blueprint
    from .views import data_view
    
    # Bluepint 등록
    app.register_blueprint(data_view.dataBP)
    
    ## 테스트 기능
    with app.test_request_context():
        print(url_for("static", filename="css/style_1.css"))
        print(url_for("static", filename="img/mine.jpg"))
    
    ## Flask Server 인스턴스 반환
    return app