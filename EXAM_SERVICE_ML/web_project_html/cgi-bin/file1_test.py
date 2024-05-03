### 모듈 로딩
import cgi, sys, codecs, datetime
from PIL import Image
import torchvision.transforms as transforms
import torch


### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


### 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서 저장하고 있는 인스턴스
form = cgi.FieldStorage()

if 'img_file' in form : 
    fileitem = form['img_file']   # 이미지 파일을 꺼낸다.
    img_file = fileitem.filename  # 이미지 파일 이름을 꺼낸다.

    date_hour = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    save_path = f"./img/{date_hour}_{img_file}"

    with open(save_path, 'wb') as f:    # 2진수로 읽어서 쓰겠다.
        f.write(fileitem.file.read())

    img_path = f"../img/{date_hour}_{img_file}"
else : img_path = 'None'


### 요청에 대한 응답 HTML
print("Content-Type : text/html")    
print()
print("<TITLE>Let's check</TITLE>")
print(f"<img src = {img_path}>")       # 이미지 로딩함


# python -m http.server 8080 --bind 127.0.0.1 --cgi