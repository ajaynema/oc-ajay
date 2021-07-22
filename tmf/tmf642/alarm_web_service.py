import sys, os.path

sys.path.append("./../../db")

from flask import Flask,Response,request
import jsonpickle
from db_manager import DbManager
BASE_URL="/tmf-api/alarmManagement/<version>"
class AlarmWebService:
    def __init__(self,name="AlarmWebService",port=80):
        self.name = name
        self.api = Flask(self.name)  
        #Single Alarm Operations
        self.api.add_url_rule(BASE_URL+"/alarm","create_alarm",self.create_alarm,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/alarm/<alarmId>","modify_alarm",self.modify_alarm,methods=['PATCH'])
        self.api.add_url_rule(BASE_URL+"/alarm/<alarmId>","delete_alarm",self.delete_alarm,methods=['DELETE'])
        self.api.add_url_rule(BASE_URL+"/alarm/<alarmId>","get_alarm",self.get_alarm,methods=['GET'])
        #Multiple Alarms Operations
        self.api.add_url_rule(BASE_URL+"/alarms","get_alarms",self.get_alarms,methods=['GET'])
        self.api.add_url_rule(BASE_URL+"/alarm","get_alarms",self.get_alarms,methods=['GET'])
        self.api.add_url_rule(BASE_URL+"/ackAlarms","ack_alarms",self.ack_alarms,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/unAckAlarms","unack_alarms",self.unack_alarms,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/clearAlarms","clear_alarms",self.clear_alarms,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/commentsAlarms","comment_alarms",self.comment_alarms,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/groupAlarms","group_alarms",self.group_alarms,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/ungroupAlarms","ungroup_alarms",self.ungroup_alarms,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/hub","subscribe",self.subscribe,methods=['POST'])
        self.api.add_url_rule(BASE_URL+"/hub/<id>","unsubscribe",self.unsubscribe,methods=['DELETE'])
        self.port = port

    def create_alarm(self,version):
        data = request.get_json()
        if ("alarmType" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("perceivedSeverity" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("alarmedObject" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("sourceSystemId" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("probableCause" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("alarmRaisedTime" not in data):
            return Response("", 409 ,mimetype='application/json')
        row = DbManager.insert("DB_ALARM","alarm",data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def modify_alarm(self,version,alarmId):
       return
 
    def delete_alarm(self,version,alarmId):
        query = {"id" : alarmId}
        row = DbManager.query("DB_ALARM","alarm",query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete("DB_ALARM","alarm",alarmId)
        return Response("", 204, mimetype='application/json')
    
    def get_alarm(self,version,alarmId):
        query = {"id" : alarmId}
        row = DbManager.query("DB_ALARM","alarm",query)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def get_alarms(self,version):
        row = DbManager.get_all("DB_ALARM","alarm")
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
   
    def ack_alarms(self,version):
        return

    def unack_alarms(self,version):
        return

    def comment_alarms(self,version):
        return

    def clear_alarms(self,version):
        return

    def ungroup_alarms(self,version):
        return
    
    def group_alarms(self,version):
        return

    def subscribe(self,version):
        data = request.get_json()
        callback = data['callback']
        query = {"callback" : callback}
        row = DbManager.query("DB_PROFILE","alarm_subscription",query)
        if (row is not None):
            return Response("", 409 ,mimetype='application/json')
        row = DbManager.insert("DB_PROFILE","alarm_subscription",data)
        result={}
        result['id'] = row['id']
        result['callback'] = row['callback']
        response_str = jsonpickle.encode(result)
        print(response_str)
        return Response(response_str, 200, mimetype='application/json')

    def unsubscribe(self,version,id):
        query = {"id" : id}
        row = DbManager.query("DB_PROFILE","alarm_subscription",query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete("DB_PROFILE","alarm_subscription",id)
        return Response("", 204, mimetype='application/json')

    def start(self):
        self.api.run(host='0.0.0.0', port=self.port)

if __name__ == '__main__':
      webserice = AlarmWebService()
      webserice.start()