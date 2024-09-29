from app.views.char_checker import char_bp
from app.views.index import main
from app.views.fibo import fibo_bp

def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(fibo_bp)
    app.register_blueprint(char_bp)