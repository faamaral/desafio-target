from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class FiboForm(FlaskForm):
    number = IntegerField('Digite um número inteiro', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Enviar')

class StringForm(FlaskForm):
    string = StringField('Digite uma string', validators=[DataRequired(), Length(min=1, max=100)])
    letter = StringField('Digite uma letra', validators=[Length(min=1, max=1)], default='a')
    submit = SubmitField('Enviar')