from flask import Blueprint, render_template
from flask import current_app as app

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return render_template('main/home.html')

@main_bp.route('/about')
def about():
    return render_template('main/about.html')

