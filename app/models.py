from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    # 답변의 고유번호 - 숫자PK : 다음 번호 자동 생성
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    # Foreign key로 걸려있는 테이블에서 삭제가 발생
        # 1) answer도 같이 지운다
        # 2) answer는 남겨둔다
            # Question의 id를 남겨둔다
            # Question의 id를 지운다
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))