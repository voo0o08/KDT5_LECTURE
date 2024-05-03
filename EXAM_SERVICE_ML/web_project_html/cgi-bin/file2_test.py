### 모듈 로딩
import cgi, sys, codecs, datetime
from PIL import Image
import torchvision.transforms as transforms
import torch
import shutil

# 모델 및 엔코더 로드
import joblib
model = joblib.load('xgb_model.pkl')
encoder = joblib.load('label_encoder.pkl')

from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing
import pandas as pd
import librosa
import numpy as np
import os
import sklearn

################## html ##################

### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


### 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서 저장하고 있는 인스턴스
form = cgi.FieldStorage()

if 'audio_file' in form : 
    fileitem = form['audio_file']   # 이미지 파일을 꺼낸다.
    img_file = fileitem.filename  # 이미지 파일 이름을 꺼낸다.

    date_hour = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    save_path = f"./img/{date_hour}_{img_file}"

    # with open(save_path, 'wb') as f:    # 2진수로 읽어서 쓰겠다.
    #     f.write(fileitem.file.read())
    src_file  = f"../project/soyoung_songs/{img_file}" # 원본파일 경로(서버 기준)
    try:
        with open(src_file, 'rb') as src, open(save_path, 'wb') as dst:
            shutil.copyfileobj(src, dst)
    except:
        img_path = 'None'

    img_path = f"../img/{date_hour}_{img_file}" # cgi-bin 내부 시점 
else : img_path = 'None'


### 요청에 대한 응답 HTML
print("Content-Type : text/html")    
print()
print('''<h3>~소영소영님의 결과~</h3>
    <p>audio 태그를 이용한 audio 재생 - autoplay</p>''')
print(f'''<audio controls>
      <source
        src={img_path}
        type="audio/mp3"
      />
    </audio>''')

print("<h3>이런 곡은 어떤가요?</h3>")
# print(f"<h3>~{src_file}~</h3>") # 디버깅용 -> 원본파일 경로


# python -m http.server 8080 --bind 127.0.0.1 --cgi