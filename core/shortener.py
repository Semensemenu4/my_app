from flask import Blueprint, render_template

shortener_bp = Blueprint("shortener", __name__)

@shortener_bp.route("/")
def index():
    return render_template("index.html")