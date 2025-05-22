# app.py
from flask import Flask
from core import db, login_manager
from core.models import User
from core.auth import auth_bp
from core.shortener import shortener_bp

app = Flask(__name__)
app.config.from_pyfile("config.py")

# Инициализируем расширения
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"

# Flask-Login загрузка пользователя
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Регистрируем блюпринты
app.register_blueprint(auth_bp)
app.register_blueprint(shortener_bp)
