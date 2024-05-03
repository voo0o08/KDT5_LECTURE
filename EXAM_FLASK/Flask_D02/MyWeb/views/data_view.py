## -----------------------------------------
## 역할 : 데이터 저장 및 출력 관련 웹 페이지 라우팅 처리
## URL : /input
##       /input/save 
##       /input/delete
##       /input/update 
## -----------------------------------------

## 모듈 로딩
from flask import Blueprint, render_template, request
import os
import base64

## BP instance 생성
dataBP=Blueprint('data', 
                 __name__, 
                 template_folder='templates', 
                 url_prefix="/input") 

## 라우팅 관련 함수들 
@dataBP.route('/') # dataBP prefix가 /input이니까 http://127.0.0.1:5000/input/
def input_data():
    return render_template('input_data.html', action="/input/save", method="POST") 

## GET 방식으로 데이터 저장 처리 함수
## 사용자의 요청 즉, request 객체에 데이터 저장되어 있음 
## http://127.0.0.1:5000/input/save_get
@dataBP.route('/save_get')
def save_get_data():
    # 요청 데이터 추출 
    req_dict = request.args.to_dict()
    # v = req_dict.get('value')
    # m = req_dict.get('message')
    return render_template('save_data.html', **req_dict)

## POST 방식으로 데이터 저장 처리 함수
## http://127.0.0.1:5000/input/save_post
@dataBP.route('/save_post', methods=['POST'])
def save_post_data():
    # 요청 데이터 추출 
    method = request.method
    headers = request.headers
    args = request.args.to_dict()
    v=request.form['value']
    m=request.form['message']
    return f'SAVE POST DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}<br>value : {v}<br>msg : {m}'

## save_post + save_get
## http://127.0.0.1:5000/input/save
@dataBP.route('/save', methods=['POST', 'GET'])
def save_data():
    if request.method == 'POST':
        # POST 요청 데이터 추출 
        method = request.method
        headers = request.headers
        args = request.args.to_dict()
        # 이미지 파일을 받아서 저장
        if 'img' in request.files:
            img = request.files["img"]
            img.save(os.path.join("./MyWeb/static/img/", img.filename))  # 이미지를 static 폴더에 저장
            file_path = os.path.join("../static/img/", img.filename)
            return f'''SAVE POST DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}<br><img src="{file_path}">'''
        else:
            return 'No file uploaded.'
    
    elif request.method == 'GET':
        # GET 요청 데이터 추출 
        method = request.method
        headers = request.headers
        args = request.args.to_dict()
        return f'SAVE GET DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}'
    
    return f'SAVE POST DATA : <br>METHOD : {method} <br>HEADER : {headers} <br>ARGS : {args}'