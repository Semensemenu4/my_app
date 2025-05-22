# core/models.py
from datetime import datetime
from flask_login import UserMixin
from core import db  # импортируешь db из core.__init__

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    links = db.relationship("ShortLink", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"

class ShortLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(8), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    clicks = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    def __repr__(self):
        return f"<ShortLink {self.short_code} -> {self.original_url}>"
