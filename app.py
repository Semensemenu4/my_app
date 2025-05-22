from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# from auth import auth_bp
# from shortener import shortener_bp

# app.register_blueprint(auth_bp)
# app.register_blueprint(shortener_bp)

if __name__ == "__main__":
    app.run(debug=True)
