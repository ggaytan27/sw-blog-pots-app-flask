from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/blog')
def blog():
    return render_template('blog.html')