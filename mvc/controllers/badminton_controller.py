import json
import sys
import traceback
import datetime

from flask import Flask
from flask import request


from .. import app
from .. import db
from ..models.badminton_models import *


#這裡是基本route
@app.route("/")
def hello():
    db.session.close()
    return 'This is default response'

#剛登入取得資訊
@app.route("/getaccount", methods=['GET', 'POST'])
def GetOrCreateAccount():
    try:
        db.session.expire_all()
        if request.method == 'POST':        
            data = request.get_json()

            isExists = db.session.query(db.exists().where(PlayerInfo.DeviceId == data['deviceId'])).scalar()

            if isExists:
                player = PlayerInfo.query.filter_by(DeviceId = data['deviceId']).first()        
            else:
                count = PlayerInfo.query.count()
                player = PlayerInfo()
                player.AccountId = '{0}{1}'.format('Acc',('%08d' % count))
                player.DeviceId = data['deviceId']
                db.session.add(player)
                db.session.commit()

            
        res = json.dumps({'result' : '000','accountId' : player.AccountId,'teamTemplate' : player.TeamTemplate,'firstLogin' : not isExists})   
        
    except Exception as e:
        traceback.print_exc()

    finally:
        db.session.close()

    return res


#設定揪團訊息
@app.route("/setgatherinfo", methods=['GET', 'POST'])
def SetGatherInfo():
    try:
        if request.method == 'POST':
            data = request.get_json()
            count = GatherInfo.query.count()
            gatherInfo = GatherInfo()
            gatherInfo.GatherId = '{0}{1}{2}{3}'.format('G_',data['accountId'],'_',('%010d' % count))
            gatherInfo.AccountId = data['accountId']
            gatherInfo.TeamName = data['teamName']
            gatherInfo.TeamLeader = data['teamLeader']
            gatherInfo.City = data['city']
            gatherInfo.Region = data['region']
            gatherInfo.Court = data['court']
            gatherInfo.Price = data['price']
            gatherInfo.Grade = data['grade']
            gatherInfo.PlayersCount = data['playersCount']
            gatherInfo.PlayStartDateTime = data['playStartDateTime']
            gatherInfo.PlayEndDateTime = data['playEndDateTime']
            gatherInfo.SubmitDateTime = data['submitDateTime']
            gatherInfo.LineId = data['lineId']
            gatherInfo.Phone = data['phone']
            gatherInfo.FacebookUrl = data['facebookUrl']
            gatherInfo.Information = data['information']
            db.session.add(gatherInfo)
            db.session.commit()
    except Exception as e:
        traceback.print_exc()
        return json.dumps({'result' : '100'})

    finally:
        db.session.close()

    print(gatherInfo)
    return json.dumps({'result' : '000'})


#設定城市
@app.route("/setcity", methods=['GET', 'POST'])
def SetCity():
    try:
        if request.method == 'POST':
            data = request.get_json()
            player = PlayerInfo.query.filter(AccountId = data['accountId']).first() 
            player.City = data['city']
            db.session.commit()

    except Exception as e:
        traceback.print_exc()
        return json.dumps({'result' : '100'})

    finally:
        db.session.close()

    print(gatherInfo)
    return json.dumps({'result' : '000'})

#取得球場資訊
@app.route("/getcourtsinfo", methods=['GET', 'POST'])
def GetCourtsInfo():
    try:
        if request.method == 'POST':
            data = request.get_json()
            
            lastUpdateDate = datetime.datetime.strptime(data['courtsLastUpdate'], "%Y-%m-%d %H:%M:%S")
            updateFlag = UpdateFlag.query.all()[0]
            courtflag = datetime.datetime.strptime(str(updateFlag.court_flag), "%Y-%m-%d %H:%M:%S")

            if(courtflag - lastUpdateDate).seconds > 0:
                allCourts = CourtInfo.query.all()
                courtsInfo = list()
                for court in allCourts:
                    courtsInfo.append({"courtName" : court.CourtName,"city" : court.City,"region" : court.Region,"address" : court.Address})               

                res = json.dumps({"result" : "000", "courtsInfo" : courtsInfo}, ensure_ascii=False)
            else:
                res = json.dumps({"result" : "001"})
            
    except Exception as e:
        traceback.print_exc()
        return json.dumps({'result' : '100'})

    finally:
        db.session.close()

    return res