### 모듈 로딩
import cgi, sys, codecs
import datetime

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 웹 페이지의 form 태그 내의 input 태그 입력값 가져와
# 저장하고 있는 인스턴스
form = cgi.FieldStorage() # output이 우리가 생각하는  terminal이 아니라 Web임!!

# 클라이언트의 요청 데이터 추출 
if "img_file" in form and "message" in form:
	fileitem = form["img_file"]
 
	# 서버에 이미지 파일 저장
	img_file = fileitem.filename
	
	suffix=datetime.datetime.now().strftime("%y%m%d_%H%M%S")
	
	save_path = f"./image/{suffix}_{img_file}"
	with open(save_path, "wb") as f:
		f.write(fileitem.file.read())
  
	img_path = f"../image/{suffix}_{img_file}"
	msg = form.getvalue("message")
else:
  img_path = "None"
  msg = "None"
 
# 요청에 대한 응답 HTML 
print("Content-Type: text/html; charset=utf-8")    # HTML is following
print()                             # blank line, end of headers
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print(f"Hello, world! ")

print(f"<img src={img_path}>")
print(f"<h3>{msg}</h3>")
