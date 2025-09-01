from flask import Blueprint, render_template, request

from .models import Post, User


bp = Blueprint('home', __name__, url_prefix='/')

def get_user(id):
    user = User.query.get_or_404(id)
    return user

def search_post(query):
    posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
    return posts

@bp.route('/', methods = ['GET', 'POST'])
def index():
    posts = Post.query.all()

    if request.method == 'POST':
        query = request.form.get('search')
        posts = search_post(query)
        value = 'hidden'
        return render_template('index.html', posts = posts, get_user = get_user, value = value)
    return render_template('index.html', posts = posts, get_user = get_user)

@bp.route('/blog/<url>')
def blog(url):
    post = Post.query.filter_by(url = url).first()
    return render_template('blog.html', post = post, get_user = get_user)


