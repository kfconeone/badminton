from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2es0c0rp@35.194.148.49:3306/DEMO-LOBBY-SQL-00'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2es0c0rp@35.194.148.49:3306/TestFlask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 20
db = SQLAlchemy(app)

from .controllers import *
from .models import *
