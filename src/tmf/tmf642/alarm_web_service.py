import sys, os.path

sys.path.append("./../../")
sys.path.append("./../")

from flask import Flask,Response,request
import jsonpickle
from db.db_manager import DbManager
from webservice.tmf_web_service import TmfWebService
import datetime
from alarm_event_type import AlarmEventType
from alarm_table_helper import AlarmTableHelper
from ack_alarm_table_helper import AckAlarmTableHelper
from unack_alarm_table_helper import UnackAlarmTableHelper
from group_alarm_table_helper import GroupAlarmTableHelper
from ungroup_alarm_table_helper import UngroupAlarmTableHelper
from alarm_event_table_helper import AlarmEventTableHelper
from clear_alarm_table_helper import ClearAlarmTableHelper
from comment_alarm_table_helper import CommentAlarmTableHelper
from alarm_subscription_table_helper import AlarmSubscriptionTableHelper



BASE_URL="/tmf-api/alarmManagement/<version>"


class AlarmWebService(TmfWebService):
    def __init__(self,name="AlarmWebService",port=80):
        super().__init__(name=name,port=port)
        #Single Alarm Operations
        self.register(BASE_URL+"/alarm","create_alarm",self.create_alarm,methods=['POST'])
        self.register(BASE_URL+"/alarm/<alarmId>","modify_alarm",self.modify_alarm,methods=['PATCH'])
        self.register(BASE_URL+"/alarm/<alarmId>","delete_alarm",self.delete_alarm,methods=['DELETE'])
        self.register(BASE_URL+"/alarm/<alarmId>","get_alarm",self.get_alarm,methods=['GET'])
        #Multiple Alarms Operations
        self.register(BASE_URL+"/alarms","get_alarms",self.get_alarms,methods=['GET'])
        self.register(BASE_URL+"/alarm","get_alarms",self.get_alarms,methods=['GET'])
        
        self.register(BASE_URL+"/ackAlarms","ack_alarms",self.ack_alarms,methods=['POST'])
        self.register(BASE_URL+"/ackAlarms","get_ack_alarms",self.get_ack_alarms,methods=['GET'])
        self.register(BASE_URL+"/ackAlarms/<id>","get_ack_alarm",self.get_ack_alarm,methods=['GET'])
        
        self.register(BASE_URL+"/unAckAlarms","unack_alarms",self.unack_alarms,methods=['POST'])
        self.register(BASE_URL+"/unAckAlarms","get_unack_alarms",self.get_unack_alarms,methods=['GET'])
        self.register(BASE_URL+"/unAckAlarms/<id>","get_unack_alarm",self.get_unack_alarm,methods=['GET'])
        
        self.register(BASE_URL+"/clearAlarms","clear_alarms",self.clear_alarms,methods=['POST'])
        self.register(BASE_URL+"/clearAlarms","get_clear_alarms",self.get_clear_alarms,methods=['GET'])
        self.register(BASE_URL+"/clearAlarms/<id>","get_clear_alarm",self.get_clear_alarm,methods=['GET'])
        
        self.register(BASE_URL+"/commentAlarms","comment_alarms",self.comment_alarms,methods=['POST'])
        self.register(BASE_URL+"/commentAlarms","get_comment_alarms",self.get_comment_alarms,methods=['GET'])
        self.register(BASE_URL+"/commentAlarms/<id>","get_comment_alarm",self.get_comment_alarm,methods=['GET'])
        
        self.register(BASE_URL+"/groupAlarms","group_alarms",self.group_alarms,methods=['POST'])
        self.register(BASE_URL+"/groupAlarms","get_group_alarms",self.get_group_alarms,methods=['GET'])
        self.register(BASE_URL+"/groupAlarms/<id>","get_group_alarm",self.get_group_alarm,methods=['GET'])
       
        self.register(BASE_URL+"/ungroupAlarms","ungroup_alarms",self.ungroup_alarms,methods=['POST'])
        self.register(BASE_URL+"/ungroupAlarms","get_ungroup_alarms",self.get_ungroup_alarms,methods=['GET'])
        self.register(BASE_URL+"/ungroupAlarms/<id>","get_ungroup_alarm",self.get_ungroup_alarm,methods=['GET'])
       
        self.register(BASE_URL+"/hub","subscribe",self.subscribe,methods=['POST'])
        self.register(BASE_URL+"/hub","get_subscribe",self.get_subscribe,methods=['GET'])
        self.register(BASE_URL+"/hub/<id>","unsubscribe",self.unsubscribe,methods=['DELETE'])
        
        
    def create_event(self,eventType,event_data):
        event = {}
        event['eventType']  = eventType.name
        event['event'] = event_data
        event['eventTime'] = self.get_formated_time()
        event['status'] = "pending"
        AlarmEventTableHelper().insert(event)

    def create_alarm(self,version):
        data = request.get_json()
        print(data)
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
        row = AlarmTableHelper().insert(data)
        self.create_event(AlarmEventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def modify_alarm(self,version,alarmId):
       data = request.get_json()
       self.create_event(AlarmEventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(AlarmTableHelper(),alarmId,data)

    def delete_alarm(self,version,alarmId):
        query = {"id" : alarmId}
        row = AlarmTableHelper().get_by_id(id)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        AlarmTableHelper().delete(alarmId)
        self.create_event(AlarmEventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')
    
    def get_alarm(self,version,alarmId):
        return self.get_by_id(AlarmTableHelper(),alarmId)

    def get_alarms(self,version):
        return self.get_all(AlarmTableHelper())
    
    def get_ack_alarm(self,version,id):
        return self.get_by_id(AckAlarmTableHelper(),id)
    
    def get_ack_alarms(self,version):
        return self.get_all(AckAlarmTableHelper())
  
    def get_unack_alarms(self,version):
        return self.get_all(UnackAlarmTableHelper())
   
    def get_unack_alarm(self,version,id):
        return self.get_by_id(UnackAlarmTableHelper(),id)
 
    def get_clear_alarms(self,version):
        return self.get_all(ClearAlarmTableHelper())
   
    def get_clear_alarm(self,version,id):
        return self.get_by_id(ClearAlarmTableHelper(),id)
 
    def get_comment_alarms(self,version):
        return self.get_all(CommentAlarmTableHelper())
   
    def get_comment_alarm(self,version,id):
        return self.get_by_id(CommentAlarmTableHelper(),id)

    def get_group_alarms(self,version):
       return self.get_all(GroupAlarmTableHelper())
   
    def get_group_alarm(self,version,id):
        return self.get_by_id(GroupAlarmTableHelper(),id)
 
    def get_ungroup_alarms(self,version):
        return self.get_all(UngroupAlarmTableHelper())
   
    def get_ungroup_alarm(self,version,id):
        return self.get_by_id(UngroupAlarmTableHelper(),id)
 
    def get_subscribe(self,version):
        return self.get_all(AlarmSubscriptionTableHelper())

    def process_unack(self,ack_alarm):
        alarmPattern = ack_alarm['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = AlarmTableHelper().query_many(query) 
        ack_alarm['unackedAlarm'] = [] 
        for row in alarms:
             alarm = {}
             alarm['id'] = row['id']
             alarm['ackSystemId'] = ack_alarm['ackSystemId']
             alarm['ackUserId'] = ack_alarm['ackUserId']
             row['id'] = row['id']
             row['ackSystemId'] = ack_alarm['ackSystemId']
             row['ackUserId'] = ack_alarm['ackUserId']
             if 'ackTime' in ack_alarm:
                alarm['ackTime'] = ack_alarm['ackTime']
                row['ackTime'] = ack_alarm['ackTime']
                 
             alarm['ackState'] = "UNacknowledged"
             row['ackState'] = "UNacknowledged"
             alarm = AlarmTableHelper().update(row['id'],alarm)
             ack_alarm['unackedAlarm'].append(row)
        ack_alarm['state'] = 'done'  
        UnackAlarmTableHelper().update(ack_alarm['id'],ack_alarm)
        return
    
    def process_ack(self,ack_alarm):
        alarmPattern = ack_alarm['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = AlarmTableHelper().query_many(query)
        ack_alarm['ackedAlarm'] = [] 
        for row in alarms:
             alarm = {}
             alarm['id'] = row['id']
             alarm['ackSystemId'] = ack_alarm['ackSystemId']
             alarm['ackUserId'] = ack_alarm['ackUserId']
             row['id'] = row['id']
             row['ackSystemId'] = ack_alarm['ackSystemId']
             row['ackUserId'] = ack_alarm['ackUserId']
             if 'ackTime' in ack_alarm:
                alarm['ackTime'] = ack_alarm['ackTime']
                row['ackTime'] = ack_alarm['ackTime']
                 
             alarm['ackState'] = "acknowledged"
             row['ackState'] = "acknowledged"
             AlarmTableHelper().update(row['id'],alarm)
             ack_alarm['ackedAlarm'].append(row)
        ack_alarm['state'] = 'done'  
        AckAlarmTableHelper().update(ack_alarm['id'],ack_alarm)
        return

    def process_clear(self,request):
        alarmPattern = request['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = AlarmTableHelper().query_many(query)
        request['clearedAlarm'] = [] 
        for row in alarms:
             alarm = {}
             alarm['id'] = row['id']
             alarm['clearSystemId'] = request['clearSystemId']
             alarm['clearUserId'] = request['clearUserId']
             row['id'] = row['id']
             row['clearSystemId'] = request['clearSystemId']
             row['clearUserId'] = request['clearUserId']
             if 'alarmClearedTime' in request:
                alarm['alarmClearedTime'] = request['alarmClearedTime']
                row['alarmClearedTime'] = request['alarmClearedTime']
                 
             alarm['state'] = "cleared"
             alarm['perceivedSeverity'] = "cleared"
             
             row['state'] = "cleared"
             row['perceivedSeverity'] = "cleared"
             AlarmTableHelper().update(row['id'],alarm)
             request['clearedAlarm'].append(row)
        request['state'] = 'done'  
        ClearAlarmTableHelper().update(request['id'],request)
        return
    
    def process_group(self,request):
        alarmPattern = request['correlatedAlarm']
        query =  {"$or" : alarmPattern}
        alarms = AlarmTableHelper().query_many(query)  
        request['groupedAlarm'] = [] 
        query =  request['parentAlarm']
        parent_alarm = AlarmTableHelper().query(query)  
        if 'correlatedAlarm' not in parent_alarm:
                parent_alarm['correlatedAlarm'] = []
        request['groupedAlarm'] = [] 
        for row in alarms:
             if 'parentAlarm' not in row:
                row['parentAlarm'] = []
             row['parentAlarm'].append(request['parentAlarm'])
             alarm = {}
             alarm['id'] = row['id']
             alarm['parentAlarm'] = []
             for c in row['parentAlarm']:
                alarm['parentAlarm'].append(c)
             AlarmTableHelper().update(row['id'],alarm)
             request['groupedAlarm'].append(row)
             parent_alarm['correlatedAlarm'].append(row)
        request['state'] = 'done' 
        request['groupedAlarm'].append(parent_alarm)
        AlarmTableHelper().update(parent_alarm['id'],parent_alarm) 
        GroupAlarmTableHelper().update(request['id'],request)
        return
    
    def process_ungroup(self,request):
        alarmPattern = request['correlatedAlarm']
        query =  {"$or" : alarmPattern}
        alarms = AlarmTableHelper().query_many(query)  
        request['ungroupedAlarm'] = [] 
        query =  request['parentAlarm']
        parent_alarm = AlarmTableHelper().query(query)  
        #Remove the parent
        for row in alarms:
             if 'parentAlarm' not in row:
                continue
             parentrows = []
             for parentRow in row['parentAlarm']:
                 if (parentRow['id'] == parent_alarm['id']):
                     continue
                 parentrows.append(parentRow)
             row['parentAlarm'] = parentrows
             alarm = {}
             alarm['id'] = row['id']
             alarm['parentAlarm'] = []
             for c in row['parentAlarm']:
                alarm['parentAlarm'].append(c)
             AlarmTableHelper().update(row['id'],alarm)
             request['ungroupedAlarm'].append(row)
        #remove the correlated alarms
        parent_alarm["correlatedAlarm"] = []
        for row in alarms:
            for correlateRow in row['correlatedAlarm']:
                if (row['id'] == correlateRow['id']):
                    continue
                parent_alarm["correlatedAlarm"].append(correlateRow)
        request['state'] = 'done' 
        request['ungroupedAlarm'].append(parent_alarm)
        AlarmTableHelper().update(parent_alarm['id'],parent_alarm) 
        UngroupAlarmTableHelper().update(request['id'],request)
        return

    def process_comment(self,request):
        alarmPattern = request['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = AlarmTableHelper().query_many(query) 
        request['commentedAlarm'] = [] 
        for row in alarms:
             if 'comment' not in row:
                 row['comment'] = []
             row['comment'].append(request['comment'])
             alarm = {}
             alarm['id'] = row['id']
             alarm['comment']=[]
             for c in row['comment']:
                alarm['comment'].append(c)
             row['id'] = row['id'] 
             AlarmTableHelper().update(row['id'],alarm)
             request['commentedAlarm'].append(row)
             print("\n\nalarm:")
             print(alarm)
        request['state'] = 'done'  
        CommentAlarmTableHelper().update(request['id'],request)
        return
    
    def ack_alarms(self,version):
        data = request.get_json()
        if ("ackSystemId" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("ackUserId" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("alarmPattern" not in data):
            return Response("", 409 ,mimetype='application/json')
        data['state'] = "progress"
        row = AckAlarmTableHelper().insert(data)
        self.process_ack(row)
        response_str = jsonpickle.encode(row)
        self.create_event(AlarmEventType.AckAlarmsCreateEvent,data)
        return Response(response_str, 200, mimetype='application/json')
   
    def unack_alarms(self,version):
        data = request.get_json()
        if ("ackSystemId" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("ackUserId" not in data):
            return Response("", 409 ,mimetype='application/json')
        if ("alarmPattern" not in data):
            return Response("", 409 ,mimetype='application/json')
        data['state'] = "progress"
        row = UnackAlarmTableHelper().insert(data)
        self.process_unack(row)
        self.create_event(AlarmEventType.UnAckAlarmsCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def comment_alarms(self,version):
        data = request.get_json()
        print(data)
        if ("comment" not in data):
            print(" missing comment")
            return Response("", 409 ,mimetype='application/json')
        if ("alarmPattern" not in data):
            print(" missing alarmPattern")
            return Response("", 409 ,mimetype='application/json')
        data['state'] = "progress"
        row = CommentAlarmTableHelper().insert(data)
        self.process_comment(row)
        self.create_event(AlarmEventType.CommentAlarmsCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def clear_alarms(self,version):
        data = request.get_json()
        print(data)
        if ("clearSystemId" not in data):
            print(" missing clearSystemId")
            return Response("", 409 ,mimetype='application/json')
        if ("clearUserId" not in data):
            print(" missing clearUserId")
            return Response("", 409 ,mimetype='application/json')
        if ("alarmPattern" not in data):
            print(" missing alarmPattern")
            return Response("", 409 ,mimetype='application/json')
        data['state'] = "progress"
        row = ClearAlarmTableHelper().insert(data)
        self.process_clear(row)
        self.create_event(AlarmEventType.ClearAlarmsCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def group_alarms(self,version):
        data = request.get_json()
        if ("sourceSystemId" not in data):
            print(" missing sourceSystemId")
            return Response("", 409 ,mimetype='application/json')
        if ("alarmChangedTime" not in data):
            print(" missing clearSystemId")
            return Response("", 409 ,mimetype='application/json')
        if ("parentAlarm" not in data):
            print(" missing clearUserId")
            return Response("", 409 ,mimetype='application/json')
        if ("correlatedAlarm" not in data):
            print(" missing alarmPattern")
            return Response("", 409 ,mimetype='application/json')
        data['state'] = "progress"
        row = GroupAlarmTableHelper().insert(data)
        self.process_group(row)
        self.create_event(AlarmEventType.GroupAlarmsCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def ungroup_alarms(self,version):
        data = request.get_json()
        if ("sourceSystemId" not in data):
            print(" missing sourceSystemId")
            return Response("", 409 ,mimetype='application/json')
        if ("alarmChangedTime" not in data):
            print(" missing clearSystemId")
            return Response("", 409 ,mimetype='application/json')
        if ("parentAlarm" not in data):
            print(" missing clearUserId")
            return Response("", 409 ,mimetype='application/json')
        if ("correlatedAlarm" not in data):
            print(" missing correlatedAlarm")
            return Response("", 409 ,mimetype='application/json')
        data['state'] = "progress"
        row = UngroupAlarmTableHelper().insert(data)
        self.process_ungroup(row)
        self.create_event(AlarmEventType.UnGroupAlarmsCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')


    def subscribe(self,version):
        data = request.get_json()
        callback = data['callback']
        query = {"callback" : callback}
        row = AlarmSubscriptionTableHelper.query(query)
        if (row is not None):
            return Response("", 409 ,mimetype='application/json')
        row = AlarmSubscriptionTableHelper().insert(data)
        result={}
        result['id'] = row['id']
        result['callback'] = row['callback']
        response_str = jsonpickle.encode(result)
        print(response_str)
        return Response(response_str, 200, mimetype='application/json')

    def unsubscribe(self,version,id):
        row = UnackAlarmTableHelper().get_by_id(id)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        AlarmSubscriptionTableHelper().delete(id)
        return Response("", 204, mimetype='application/json')

if __name__ == '__main__':
      webserice = AlarmWebService()
      webserice.start()