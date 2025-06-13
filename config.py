SQLITE = "sqlite:///project.db"
POSTGRESQL = ""


class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = SQLITE