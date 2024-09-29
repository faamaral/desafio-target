from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@main.route('/index', methods=['GET'])
def index():
    return render_template('index.html')