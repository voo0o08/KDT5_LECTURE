# 모듈로딩 -----------------------------------
from flask import Blueprint, request
from YouWEB.models import Question
from flask import render_template
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

# BP 인스턴스 생성 ----------------------------
bp = Blueprint('main', 
               __name__,
               template_folder='templates',
               url_prefix = '/')

# 라우팅 함수들
@bp.route('/')
def index(): 
    # Question 테이블에 저장된 데이터 읽어서 출력 
    q_list = Question.query.order_by(Question.create_date.desc())
    print('q_list => {q_list}')
    return render_template('q_list.html', questions=q_list)
    # return f"<h3>HI ~^^</h3> {q_list}"
    
# 질문 입력
@bp.route('/question/create')
def create_question(): 
    return render_template('q_create.html')

# 질문 입력 후 DB에 저장 
@bp.route('/save', methods=['POST'])
def save_question(): 
    if request.method == 'POST':
        # 폼에서 입력한 데이터 받기
        title = request.form['title']
        content = request.form['content']
        # return f"{title} {content}"
        # subject,content
        # 데이터베이스에 데이터 저장
        new_question = Question(subject=title, content=content, create_date=datetime.now())
        db.session.add(new_question)
        db.session.commit()
    q_list = Question.query.order_by(Question.create_date.desc())
    print('q_list => {q_list}')
    return render_template('q_list.html', questions=q_list)