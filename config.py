DEBUG = True

USERNAME = 'root'
PASSWORD = 'Wam293031@'
SERVER = 'localhost'
DB = 'flask_fundamentos_crud'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "da17fbb8722c0771098cbb0557e2ad72"
