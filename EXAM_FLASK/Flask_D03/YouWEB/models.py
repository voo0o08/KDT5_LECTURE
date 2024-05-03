# # 모듈 로딩 ---------------------------
# from YouWEB import db

# ## Question 테이블 클래스
# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     subject = db.Column(db.String(200), nullable = False)
#     content = db.Column(db.Text(), nullable = False)
#     create_date = db.Column(db.DateTime(), nullable = False)
    
# ## Answer 테이블 클래스
# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     question_id = db.Column(db.Integer, db.ForeingKey('question.id', ondelete='CASCADE'))
#     question = db.relationship('Question', backref=db.backref('answer_set'))
#     content = db.Column(db.Text(), nullable = False) 
#     create_data = db.Column(db.DateTime(), nullable = False)   
from YouWEB import db

class Question(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question_id=db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question=db.relationship('Question', backref=db.backref('answer_set'))
    content=db.Column(db.Text(), nullable=False)
    create_date=db.Column(db.DateTime(), nullable=False)
