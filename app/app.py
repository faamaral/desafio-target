from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

from app import views

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

def create_app():
    app = Flask(__name__)
    app.secret_key = 'a12qffsrwwq423313'
    bootstrap = Bootstrap5(app)
    csrf = CSRFProtect(app)
    views.init_app(app)
    return app

app = create_app()