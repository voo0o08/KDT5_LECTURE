## 모듈 로딩
from flask import Blueprint, render_template, request
import os
import base64

# 모델 로드 및 데이터 처리 ===============================================================
# 모델 및 엔코더 로드
import joblib
model = joblib.load('./MyWeb/static/model/xgb_model.pkl')
encoder = joblib.load('./MyWeb/static/model/label_encoder.pkl')

from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing
import pandas as pd
import librosa
import numpy as np
import os
import sklearn

def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)

def classifier(file_path_audio):
# if 'audio_file' in form : 
    # fileitem = form['audio_file']   # 이미지 파일을 꺼낸다.
    # img_file = fileitem.filename  # 이미지 파일 이름을 꺼낸다.

    # date_hour = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    # save_path = f"./img/{date_hour}_{img_file}"

    # with open(save_path, 'wb') as f:    # 2진수로 읽어서 쓰겠다.
    #     f.write(fileitem.file.read())
    # src_file  = f"../project/soyoung_songs/{img_file}" # 원본파일 경로(서버 기준)
    try:
        # with open(src_file, 'rb') as src, open(save_path, 'wb') as dst:
        #     shutil.copyfileobj(src, dst)
        
        # img_path = f"../img/{date_hour}_{img_file}" # cgi-bin 내부 시점 
        ## 머신러닝 부분
        # DataFrame을 저장할 빈 리스트 생성
        df_list = []
        so_result = file_path_audio # 소영언니의 분석 결과
        
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
        return genre
		
    except:
        img_path = 'None'
        

# =======================================================================================


## BP instance 생성
dataBP=Blueprint('data', 
                 __name__, 
                 template_folder='templates', 
                 url_prefix="/input") 

## 라우팅 관련 함수들 
@dataBP.route('/') # dataBP prefix가 /input이니까 http://127.0.0.1:5000/input/
def input_data():
    return render_template('HW2_h.html', action="/input/save", method="POST") # HTML내의 {{action}}, {{method}}안에 뭐가 들어갈지 설정  

## save_post + save_get
## http://127.0.0.1:5000/input/save
@dataBP.route('/save', methods=['POST', 'GET'])
def save_data():
    if request.method == 'POST':
        # POST 요청 데이터 추출 
        method = request.method
        headers = request.headers
        args = request.args.to_dict()
        # return f'SAVE POST DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}'
        # 이미지 파일을 받아서 저장
        if 'audio' in request.files:
            # # img
            # img = request.files["img"]
            # img.save(os.path.join("./MyWeb/static/img/", img.filename))  # 이미지를 static 폴더에 저장
            # file_path_img = os.path.join("../static/img/", img.filename)
            
            # audio
            audio = request.files["audio"]
            audio.save(os.path.join("./MyWeb/static/music/", audio.filename))  # 이미지를 static 폴더에 저장
            file_path_audio = os.path.join("../static/music/", audio.filename)
            # SAVE POST DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}<br><img src="{file_path_img}">
            genre_result = classifier(os.path.join("./MyWeb/static/music/", audio.filename))
            return f'''<h1>해당 곡의 장르는 {genre_result}입니다!</h1><audio controls autoplay="autoplay">
                        <source src={file_path_audio} type="audio/mpeg" /></audio>'''
        else:
            return 'No file uploaded.'
    
    elif request.method == 'GET':
        # GET 요청 데이터 추출 
        method = request.method
        headers = request.headers
        args = request.args.to_dict()
        return f'SAVE GET DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}'
    
    return f'SAVE POST DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}'