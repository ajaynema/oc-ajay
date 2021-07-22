from flask import Flask,Response,request
import jsonpickle
from json import JSONEncoder
import json

class AlarmWebService:
    def __init__(self,name="AlarmWebService",port=80):
        self.name = name
        self.api = Flask(self.name)  
        #Single Alarm Operations
        self.api.add_url_rule("/api/<version>/alarm","create_alarm",self.create_alarm,methods=['POST'])
        self.api.add_url_rule("/api/<version>/alarm/<alarmId>","modify_alarm",self.modify_alarm,methods=['PATCH'])
        self.api.add_url_rule("/api/<version>/alarm/<alarmId>/clear","clear_alarm",self.modify_alarm,methods=['POST'])
        self.api.add_url_rule("/api/<version>/alarm/<alarmId>","get_alarm",self.get_alarm,methods=['GET'])
        #Multiple Alarms Operations
        self.api.add_url_rule("/api/<version>/alarms","get_alarms",self.get_alarms,methods=['GET'])
        self.api.add_url_rule("/api/<version>/ackAlarms","ack_alarms",self.ack_alarms,methods=['POST'])
        self.api.add_url_rule("/api/<version>/unAckAlarms","unack_alarms",self.unack_alarms,methods=['POST'])
        self.api.add_url_rule("/api/<version>/clearAlarms","clear_alarms",self.clear_alarms,methods=['POST'])
        self.api.add_url_rule("/api/<version>/commentsAlarms","comment_alarms",self.comment_alarms,methods=['POST'])
        self.api.add_url_rule("/api/<version>/groupAlarms","group_alarms",self.group_alarms,methods=['POST'])
        self.api.add_url_rule("/api/<version>/ungroupAlarms","ungroup_alarms",self.ungroup_alarms,methods=['POST'])
        #Subscribe PUB/SUB
        self.api.add_url_rule("/api/<version>/hub","subscribe",self.subscribe,methods=['POST'])
        self.api.add_url_rule("/api/<version>/hub/<id>","hub",self.unsubscribe,methods=['DELETE'])
        self.port = port

    def create_alarm(self,version):
        return

    def modify_alarm(self,version,alarmId):
        return

    def clear_alarm(self,version,alarmId):
        return
    
    def get_alarm(self,version,alarmId):
        return

    def get_alarms(self,version):
        return

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
        return
    def unsubscribe(self,version,id):
        return

    def start(self):
        self.api.run(host='0.0.0.0', port=self.port)

if __name__ == '__main__':
      webserice = AlarmWebService()
      webserice.start()