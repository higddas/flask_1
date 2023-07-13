from flask import Blueprint, render_template, request, url_for

from app.models import Question,Answer
from app import db
from app.forms import AnswerForm
from datetime import datetime
from werkzeug.utils import redirect

                # 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
answer = Blueprint('answer', __name__, url_prefix='/answer')

@answer.route('/detail/<int:question_id>')
def create(question_id):
    # 입력양식에 데이터를 입력
    form = AnswerForm()
    # 로그인 한 경우/ 로그인 하지 않은 경우
    question = Question.query.all(question_id)
    if form.validate_on_submit():
        a = Answer(content=form.content.data, create_date=datetime.now())
        question.answer_set.append(a)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)
