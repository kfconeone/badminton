from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .. import db




class User(db.Model):
    __tablename__ = 'User'

    name = db.Column(db.String(50), primary_key=True)
    age = db.Column(db.Integer, nullable=False)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False, unique=True, server_default='')


