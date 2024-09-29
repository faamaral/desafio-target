from flask import Blueprint, request, render_template

from app.forms.forms import StringForm
from app.utils.char import char_checker

char_bp = Blueprint('char', __name__)

@char_bp.route('/char_checker', methods=['GET', 'POST'])
def index():
    form = StringForm()
    if form.validate_on_submit():
        string=form.string.data
        letter = None
        if form.letter.data is not None:
            letter=form.letter.data
        result = char_checker(string, letter=letter)
        if result > 0:
            return render_template('char.html', form=form, message=f'A letra \'{letter}\' apareceu na string {result} vezes')
        else:
            return render_template('char.html', form=form, message=f'A string não contem a letra \'{letter}\'')
    return render_template('char.html', form=form)