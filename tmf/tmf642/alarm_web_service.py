from flask import Flask,Response,request
import jsonpickle
from json import JSONEncoder
import json

class AlarmWebService:
    def __init__(self,name="AlarmWebService",port=80):
        self.name = name
        self.api = Flask(self.name)  
        #Single Alarm Operations
        self.api.add_url_rule("/alarm","create_alarm",self.create_alarm,methods=['POST'])
        self.api.add_url_rule("/alarm/<alarmId>","modify_alarm",self.modify_alarm,methods=['PATCH'])
        self.api.add_url_rule("/alarm/<alarmId>/clear","clear_alarm",self.modify_alarm,methods=['POST'])
        self.api.add_url_rule("/alarm/<alarmId>","get_alarm",self.get_alarm,methods=['GET'])
        #Multiple Alarms Operations
        self.api.add_url_rule("/alarms","get_alarms",self.get_alarms,methods=['GET'])
        self.api.add_url_rule("/ackAlarms","ack_alarms",self.ack_alarms,methods=['POST'])
        self.api.add_url_rule("/unAckAlarms","unack_alarms",self.unack_alarms,methods=['POST'])
        self.api.add_url_rule("/clearAlarms","clear_alarms",self.clear_alarms,methods=['POST'])
        self.api.add_url_rule("/commentsAlarms","comment_alarms",self.comment_alarms,methods=['POST'])
        self.api.add_url_rule("/groupAlarms","group_alarms",self.group_alarms,methods=['POST'])
        self.api.add_url_rule("/ungroupAlarms","ungroup_alarms",self.ungroup_alarms,methods=['POST'])
        self.port = port

    def create_alarm(self):
        return

    def modify_alarm(self, alarmId):
        return

    def clear_alarm(self, alarmId):
        return
    
    def get_alarm(self, alarmId):
        return

    def get_alarms(self):
        return

    def ack_alarms(self):
        return

    def unack_alarms(self):
        return

    def comments_alarms(self):
        return

    def ungroup_alarms(self):
        return
    
    def group_alarms(self):
        return

    def start(self):
        self.api.run(host='0.0.0.0', port=self.port)

if __name__ == '__main__':
      webserice = AlarmWebService()
      webserice.start()