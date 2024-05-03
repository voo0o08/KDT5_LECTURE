### 모듈 로딩
import cgi, sys, codecs, datetime
from PIL import Image
import torchvision.transforms as transforms
import torch
import shutil

# 모델 및 엔코더 로드
import joblib
model = joblib.load('./cgi-bin/xgb_model.pkl')
encoder = joblib.load('./cgi-bin/label_encoder.pkl')

from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing
import pandas as pd
import librosa
import numpy as np
import os
import sklearn

def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)

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
            
        ## 머신러닝 부분
        # DataFrame을 저장할 빈 리스트 생성
        df_list = []
        so_result = src_file # 소영언니의 분석 결과
        
        # WAV 파일 로드
        y, sr = librosa.load(so_result)

		# MFCCs 계산
        mfccs = librosa.feature.mfcc(y=y, sr=sr)
        mfccs = normalize(mfccs, axis=1)
        mfcc_mean_list = []
        mfcc_var_list = []
        for i, mfcc_line in enumerate(mfccs[::-1]):
            mfcc_mean_list.append(np.mean(mfcc_line))
            mfcc_var_list.append(np.var(mfcc_line))
            if i == 9:
                break

		# Spectral Centroids 계산
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

		# Spectral Rolloff 계산
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]

		# Chromagram 계산
        chromagram = librosa.feature.chroma_stft(y=y, sr=sr, hop_length=512)

		# Zero-Crossing Rate (제로 크로싱 비율)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]

		# Root Mean Square (RMS) Energy (평균 제곱근 에너지)
        rms_energy = librosa.feature.rms(y=y)[0]

		# Spectral Bandwidth (주파수 대역폭)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]

		# Spectral Contrast (주파수 대비)
        spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)

		# Spectral Flatness (주파수 평평도)
        spectral_flatness = librosa.feature.spectral_flatness(y=y)

		# BPM 계산
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

		# 하모니(음색) -> 코러스 좀... / 충격파(둥둥)
        harmonic, percussive = librosa.effects.hpss(y=y)

		# 각 특징들의 평균과 분산 계산
        data = {
			'Filename': so_result,
			'MFCC_Mean': [np.mean(mfccs)],
			'MFCC_Var': [np.var(mfccs)],
			'Chromagram_Mean': [np.mean(chromagram)],
			'Chromagram_Var': [np.var(chromagram)],
			'Spectral_Centroids_Mean': [np.mean(spectral_centroids)],
			'Spectral_Centroids_Var': [np.var(spectral_centroids)],
			'Spectral_Rolloff_Mean': [np.mean(spectral_rolloff)],
			'Spectral_Rolloff_Var': [np.var(spectral_rolloff)],
			'Zero_Crossing_Rate': [np.mean(zero_crossing_rate)],
			'RMS_Energy_Mean': [np.mean(rms_energy)],
			'RMS_Energy_Var': [np.var(rms_energy)],
			'Spectral_Bandwidth_Mean': [np.mean(spectral_bandwidth)],
			'Spectral_Bandwidth_Var': [np.var(spectral_bandwidth)],
			'Spectral_Contrast_Mean': [np.mean(spectral_contrast)],
			'Spectral_Contrast_Var': [np.var(spectral_contrast)],
			'Spectral_Flatness_Mean': [np.mean(spectral_flatness)],
			'Spectral_Flatness_Var': [np.var(spectral_flatness)],
			'Tempo': [tempo],

			"harmony_mean": [harmonic.mean()],
			"harmony_var": [harmonic.var()],
			"precussive_mean": [percussive.mean()],
			"percussive_var": [percussive.var()],
			'label': 0 # 장르는 임시로
		}

		# 데이터를 DataFrame으로 변환하여 리스트에 추가
        df_list.append(pd.DataFrame(data))

		# 모든 DataFrame을 하나의 큰 DataFrame으로 결합
        new_df = pd.concat(df_list, ignore_index=True)

		# 예측
        featureDF = new_df.drop(columns=['label', "Filename"])
        genre = encoder.inverse_transform(model.predict(featureDF))[0]
        
        
  
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
print(f"<h3>{genre}장르의 곡이 잘 어울려요~</h3>")
print("<h3>이런 곡은 어떤가요?</h3>")
print(f"<h3>~{src_file}~</h3>") # 디버깅용 -> 원본파일 경로


# python -m http.server 8080 --bind 127.0.0.1 --cgi