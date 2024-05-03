### 모듈 로딩 
from flask import Flask, render_template, Blueprint

### 어플리케이션 팩토리 
def create_app():
    myapp=Flask(__name__)
    
    # bp등록
    from .views import main_views
    myapp.register_blueprint(main_views.bp)
    
    return myapp
# ### 전역변수
# myapp = Flask(__name__)

# ### 사용자 요청 URL 처리 기능 -> 라우팅(Routing)
# ### 형식 : @Flask_instance_name.route(URL 문자열)

# ### 웹 서버의 첫 페이지 : http://127.0.0.1:5000/ -> 생략
# @myapp.route('/')
# def index_page():
#     # return "<h3><font color='green'>My Web Index Page</font></h3>"
#     return render_template("tem.html")

# ### 사용자마다 페이지 반환 
# ### 사용자 페이지 URL : http://127.0.0.1:5000/<username>
# @myapp.route('/<name>') 
# # 라우팅 함수
# def username(name):
#     return f"username : {name}pang"

# @myapp.route("/<int:number>")
# def show_number(number):
#     return f"Select Number : {number}"

# @myapp.route("/hello") # /hello랑 /hello/랑 다름 
# def hello():
#     return f"hello"

# # URL이동 -> user_info2로 들어가면 초기화면으로 가게됨
# @myapp.route("/user_info2")
# def user_login2():
#     return myapp.redirect("/")

# ### 실행 제어
# # import된 파일이 아니라 내가 실행된 파일이라면
# if __name__ == "__main__":
#     # Flask Web server 구동
#     myapp.run(debug=True) # 주소가 나왔을 때 보여줄 내용을 만들어 줘야함 404-