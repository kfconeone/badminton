# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class CourtInfo(db.Model):
    __tablename__ = 'Court_Info'

    CourtName = db.Column(db.String(50), primary_key=True)
    City = db.Column(db.String(50), nullable=False)
    Region = db.Column(db.String(50), nullable=False)
    Address = db.Column(db.String(50), nullable=False)


class ErrorInfo(db.Model):
    __tablename__ = 'Error_Info'

    id = db.Column(db.Integer, primary_key=True)
    OccurTime = db.Column(db.DateTime, nullable=False)
    Message = db.Column(db.Text, nullable=False)

class GatherInfo(db.Model):
    __tablename__ = 'Gather_Info'

    GatherId = db.Column(db.String(100), primary_key=True)
    AccountId = db.Column(db.ForeignKey('Player_Info.AccountId', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    TeamName = db.Column(db.String(50), nullable=False)
    TeamLeader = db.Column(db.String(50), nullable=False)
    City = db.Column(db.String(50), nullable=False)
    Region = db.Column(db.String(50), nullable=False)
    Court = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Grade = db.Column(db.String(50), nullable=False)
    PlayersCount = db.Column(db.Integer, nullable=False)
    PlayStartDateTime = db.Column(db.DateTime, nullable=False)
    PlayEndDateTime = db.Column(db.DateTime, nullable=False)
    SubmitDateTime = db.Column(db.DateTime, nullable=False)
    LineId = db.Column(db.String(50), nullable=False)
    Phone = db.Column(db.String(50), nullable=False)
    FacebookUrl = db.Column(db.String(100), nullable=False)
    Information = db.Column(db.Text, nullable=False)

    Player_Info = db.relationship('PlayerInfo', primaryjoin='GatherInfo.AccountId == PlayerInfo.AccountId', backref='gather_infos')


class JoinInfo(db.Model):
    __tablename__ = 'Join_Info'

    id = db.Column(db.Integer, primary_key=True)
    GatherId = db.Column(db.ForeignKey('Gather_Info.GatherId'), nullable=False, index=True)
    AccountId = db.Column(db.ForeignKey('Player_Info.AccountId'), nullable=False, index=True)
    Information = db.Column(db.Text)

    Player_Info = db.relationship('PlayerInfo', primaryjoin='JoinInfo.AccountId == PlayerInfo.AccountId', backref='join_infos')
    Gather_Info = db.relationship('GatherInfo', primaryjoin='JoinInfo.GatherId == GatherInfo.GatherId', backref='join_infos')


class PlayerInfo(db.Model):
    __tablename__ = 'Player_Info'

    AccountId = db.Column(db.String(50), primary_key=True)
    DeviceId = db.Column(db.String(255), nullable=False, unique=True)
    TeamTemplate = db.Column(db.Text)
    TeamTemplateHistory = db.Column(db.Text)
    City = db.Column(db.String(50), nullable=False)

class UpdateFlag(db.Model):
    __tablename__ = 'update_flag'

    court_flag = db.Column(db.DateTime, primary_key=True, server_default=db.FetchedValue())