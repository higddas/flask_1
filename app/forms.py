from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class QuestionForm(FlaskForm):
                       # label, 데이터를 보내기 위한 제약조건
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])

class AnswerForm(FlaskForm):
                       # label, 데이터를 보내기 위한 제약조건
    content = TextAreaField('답변 내용', validators=[DataRequired()])  

from wtforms import Form, BooleanField, StringField, PasswordField, validators

class UserCreateForm(FlaskForm):
    username = StringField('사용자ID', validators =[DataRequired(), Length(min=4, max=50, message="4자 이상 50자 미만")])
    password1 = PasswordField('비밀번호', validators =[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    email = StringField('Email', validators =[Length(min=6, max=100)])