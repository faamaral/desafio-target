from flask import Blueprint, render_template, request

from app.forms.forms import FiboForm
from app.utils.fibo import check_fibo

fibo_bp = Blueprint('fibo', __name__)

@fibo_bp.route('/fibo', methods=['GET', 'POST'])
def index():
    form = FiboForm()
    if form.validate_on_submit():
        fibo = check_fibo(form.number.data)
        if fibo:
            return render_template('fibo.html', message=f"O numero {request.form['number']} é um numero Fibonacci", form=form)
        else:
            return render_template('fibo.html', message=f"O numero {request.form['number']} não é um numero Fibonacci", form=form)
    return render_template('fibo.html', form=form)