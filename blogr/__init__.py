from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #crear aplicaicon
    app = Flask(__name__)

    app.config.from_object('config.Config')
    db.init_app(app)

    #importando vistas
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import posts
    app.register_blueprint(posts.bp)

    from .models import User, Post

    with app.app_context():
        db.create_all()

    return app