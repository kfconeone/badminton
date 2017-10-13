import json

from flask import Flask
from flask import request

from .. import app
from .. import db
from ..models.sample_models import *

#這裡是基本route
@app.route("/")
def hello():
    return 'This is default response'


#這裡是自訂URL的方法
@app.route("/<parameter1>")
def hello2(parameter1=None):

    return parameter1


#這裡是Post的方法
@app.route("/post", methods=['GET', 'POST'])
def post_somthing():
    if request.method == 'POST':
        data = request.get_json()
        print(data)

    return json.dumps(data)

####以下是基本SQL CRUD 基本操作####

#Create_Table
#Code-First作法，寫好Models後直接創建Tables
@app.route("/create_table")
def create_table():
    db.create_all()
    return 'Success'

#Delete_Table
#Code-First作法，會把所有的Table刪光光，危險的功能
@app.route("/delete_table")
def delete_table():
    db.drop_all()
    return 'Success'


####Create####

#Create單個欄位
@app.route("/create_data")
def create_data():
    user = User(name = "Jack",age = 15)
    db.session.add(user)
    db.session.commit()
    return 'Success'

#Create複數欄位
@app.route("/create_data_all")
def create_data_all():
    user1 = User(name = "Jack2",age = 15)
    user2 = User(name = "Jack3",age = 15)
    user3 = User(name = "Jack4",age = 15)
    db.session.add_all([user1,user2,user3])
    db.session.commit()
    return 'Success'

####Read####

#Read 其中一筆資料
@app.route("/read_data/<user_name>")
def read_data(user_name=None):
    user = User.query.filter_by(name = user_name).first()
    return json.dumps([user.name,user.age])

####Update####

#Update單個欄位
@app.route("/update_data/<user_name>/<user_age>")
def update_data():
    user = User.query.filter_by(name = user_name)
    user.age = user_age
    db.session.commit()
    return 'Success'

####Delete####

#Delete單欄位
@app.route("/delete_data/<user_name>")
def delete_data():
    user = User.query.filter_by(name = user_name)
    db.session.delete(user)
    db.session.commit()
    return 'Success'