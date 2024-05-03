### 모듈 로딩
import cgi

# 웹 페이지의 form 태그 내의 input 태그 입력값 가져와
# 저장하고 있는 인스턴스
form = cgi.FieldStorage() # output이 우리가 생각하는  terminal이 아니라 Web임!!

if "img_file" in form and "message" in form:
	filename = form["img_file"]
	msg = form["message"]
 
# 요청에 대한 응답 HTML 
print("Content-Type: text/html; charset=utf-8")    # HTML is following
print()                             # blank line, end of headers
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print(f"Hello, world! : \n{form}")
print(f"<img src={filename}>")
print(f"<h3>{msg}</h3>")