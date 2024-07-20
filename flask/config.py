import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskuser:flaskpassword@db:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


