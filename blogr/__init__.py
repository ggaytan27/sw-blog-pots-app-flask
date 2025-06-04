from flask import Flask

def create_app():
    #crear aplicaicon
    app = Flask(__name__)

    #importando vistas
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import posts
    app.register_blueprint(posts.bp)

    return app