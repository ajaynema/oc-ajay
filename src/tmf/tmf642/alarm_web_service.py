import sys, os.path

sys.path.append("./../../")
sys.path.append("./../")

from flask import Flask,Response,request
import jsonpickle
from db.db_manager import DbManager
from webservice.tmf_web_service import TmfWebService

BASE_URL="/tmf-api/alarmManagement/<version>"
DB_ALARM="DB_ALARM"
TABLE_ALARM="alarm"
TABLE_ACK_ALARM="ack_alarm"
TABLE_UNACK_ALARM="unack_alarm"
TABLE_CLEAR_ALARM="clear_alarm"
TABLE_COMMENT_ALARM="comment_alarm"
TABLE_GROUP_ALARM="group_alarm"
TABLE_UNGROUP_ALARM="ungroup_alarm"

TABLE_ALARM_SUBSCRIPTION="alarm_subscription"


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
        row = DbManager.insert(DB_ALARM,TABLE_ALARM,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    

    def modify_alarm(self,version,alarmId):
       data = request.get_json()
       return self.patch(DB_ALARM,TABLE_ALARM,alarmId,data)
    def delete_alarm(self,version,alarmId):
        query = {"id" : alarmId}
        row = DbManager.query(DB_ALARM,TABLE_ALARM,query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete(DB_ALARM,TABLE_ALARM,alarmId)
        return Response("", 204, mimetype='application/json')
    
    def get_alarm(self,version,alarmId):
        return self.get_by_id(DB_ALARM,TABLE_ALARM,alarmId)

    def get_alarms(self,version):
        return self.get_all(DB_ALARM,TABLE_ALARM)
    
    def get_ack_alarm(self,version,id):
        return self.get_by_id(DB_ALARM,TABLE_ACK_ALARM,id)
    

    def get_unack_alarms(self,version):
        return self.get_all(DB_ALARM,TABLE_UNACK_ALARM)
   
    def get_unack_alarm(self,version,id):
        return self.get_by_id(DB_ALARM,TABLE_UNACK_ALARM,id)
 
    def get_clear_alarms(self,version):
        return self.get_all(DB_ALARM,TABLE_CLEAR_ALARM)
   
    def get_clear_alarm(self,version,id):
        return self.get_by_id(DB_ALARM,TABLE_CLEAR_ALARM,id)
 
    def get_comment_alarms(self,version):
        return self.get_all(DB_ALARM,TABLE_COMMENT_ALARM)
   
    def get_comment_alarm(self,version,id):
        return self.get_by_id(DB_ALARM,TABLE_COMMENT_ALARM,id)

    def get_group_alarms(self,version):
       return self.get_all(DB_ALARM,TABLE_GROUP_ALARM)
   
    def get_group_alarm(self,version,id):
        return self.get_by_id(DB_ALARM,TABLE_GROUP_ALARM,id)
 
    def get_ungroup_alarms(self,version):
        return self.get_all(DB_ALARM,TABLE_UNGROUP_ALARM)
   
    def get_ungroup_alarm(self,version,id):
        return self.get_by_id(DB_ALARM,TABLE_UNGROUP_ALARM,id)
 
    def get_ack_alarms(self,version):
        return self.get_all(DB_ALARM,TABLE_ACK_ALARM)
    
    def get_subscribe(self,version):
        return self.get_all(DB_ALARM,TABLE_ALARM_SUBSCRIPTION)

    def process_unack(self,ack_alarm):
        alarmPattern = ack_alarm['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = DbManager.query_many(DB_ALARM,TABLE_ALARM,query) 
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
             alarm = DbManager.update(DB_ALARM,TABLE_ALARM,row['id'],alarm)
             ack_alarm['unackedAlarm'].append(row)
        ack_alarm['state'] = 'done'  
        DbManager.update(DB_ALARM,TABLE_UNACK_ALARM,ack_alarm['id'],ack_alarm)
        return
    
    def process_ack(self,ack_alarm):
        alarmPattern = ack_alarm['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = DbManager.query_many(DB_ALARM,TABLE_ALARM,query) 
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
             DbManager.update(DB_ALARM,TABLE_ALARM,row['id'],alarm)
             ack_alarm['ackedAlarm'].append(row)
        ack_alarm['state'] = 'done'  
        DbManager.update(DB_ALARM,TABLE_ACK_ALARM,ack_alarm['id'],ack_alarm)
        return

    def process_clear(self,clear_alarm):
        alarmPattern = clear_alarm['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = DbManager.query_many(DB_ALARM,TABLE_ALARM,query) 
        clear_alarm['clearedAlarm'] = [] 
        for row in alarms:
             alarm = {}
             alarm['id'] = row['id']
             alarm['clearSystemId'] = clear_alarm['clearSystemId']
             alarm['clearUserId'] = clear_alarm['clearUserId']
             row['id'] = row['id']
             row['clearSystemId'] = clear_alarm['clearSystemId']
             row['clearUserId'] = clear_alarm['clearUserId']
             if 'alarmClearedTime' in clear_alarm:
                alarm['alarmClearedTime'] = clear_alarm['alarmClearedTime']
                row['alarmClearedTime'] = clear_alarm['alarmClearedTime']
                 
             alarm['state'] = "cleared"
             alarm['perceivedSeverity'] = "cleared"
             
             row['state'] = "cleared"
             row['perceivedSeverity'] = "cleared"
             DbManager.update(DB_ALARM,TABLE_ALARM,row['id'],alarm)
             clear_alarm['clearedAlarm'].append(row)
        clear_alarm['state'] = 'done'  
        DbManager.update(DB_ALARM,TABLE_CLEAR_ALARM,clear_alarm['id'],clear_alarm)
        return
    
    def process_group(self,request):
        alarmPattern = request['correlatedAlarm']
        query =  {"$or" : alarmPattern}
        alarms = DbManager.query_many(DB_ALARM,TABLE_ALARM,query) 
        request['groupedAlarm'] = [] 
        query =  request['parentAlarm']
        parent_alarm = DbManager.query(DB_ALARM,TABLE_ALARM,query) 
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
             DbManager.update(DB_ALARM,TABLE_ALARM,row['id'],alarm)
             request['groupedAlarm'].append(row)
             parent_alarm['correlatedAlarm'].append(row)
        request['state'] = 'done' 
        request['groupedAlarm'].append(parent_alarm)
        DbManager.update(DB_ALARM,TABLE_ALARM,parent_alarm['id'],parent_alarm) 
        DbManager.update(DB_ALARM,TABLE_CLEAR_ALARM,request['id'],request)
        return
    
    def process_ungroup(self,request):
        alarmPattern = request['correlatedAlarm']
        query =  {"$or" : alarmPattern}
        alarms = DbManager.query_many(DB_ALARM,TABLE_ALARM,query) 
        request['ungroupedAlarm'] = [] 
        query =  request['parentAlarm']
        parent_alarm = DbManager.query(DB_ALARM,TABLE_ALARM,query) 
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
             DbManager.update(DB_ALARM,TABLE_ALARM,row['id'],alarm)
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
        DbManager.update(DB_ALARM,TABLE_ALARM,parent_alarm['id'],parent_alarm) 
        DbManager.update(DB_ALARM,TABLE_CLEAR_ALARM,request['id'],request)
        return

    def process_comment(self,request):
        alarmPattern = request['alarmPattern']
        query =  {"$or" : alarmPattern}
        alarms = DbManager.query_many(DB_ALARM,TABLE_ALARM,query) 
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
             DbManager.update(DB_ALARM,TABLE_ALARM,row['id'],alarm)
             request['commentedAlarm'].append(row)
             print("\n\nalarm:")
             print(alarm)
        request['state'] = 'done'  
        DbManager.update(DB_ALARM,TABLE_COMMENT_ALARM,request['id'],request)
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
        row = DbManager.insert(DB_ALARM,TABLE_ACK_ALARM,data)
        self.process_ack(row)
        response_str = jsonpickle.encode(row)
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
        row = DbManager.insert(DB_ALARM,TABLE_UNACK_ALARM,data)
        self.process_unack(row)
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
        row = DbManager.insert(DB_ALARM,TABLE_COMMENT_ALARM,data)
        self.process_comment(row)
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
        row = DbManager.insert(DB_ALARM,TABLE_CLEAR_ALARM,data)
        self.process_clear(row)
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
        row = DbManager.insert(DB_ALARM,TABLE_GROUP_ALARM,data)
        self.process_group(row)
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
        row = DbManager.insert(DB_ALARM,TABLE_GROUP_ALARM,data)
        self.process_ungroup(row)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')


    def subscribe(self,version):
        data = request.get_json()
        callback = data['callback']
        query = {"callback" : callback}
        row = DbManager.query(DB_ALARM,"alarm_subscription",query)
        if (row is not None):
            return Response("", 409 ,mimetype='application/json')
        row = DbManager.insert(DB_ALARM,TABLE_ALARM_SUBSCRIPTION,data)
        result={}
        result['id'] = row['id']
        result['callback'] = row['callback']
        response_str = jsonpickle.encode(result)
        print(response_str)
        return Response(response_str, 200, mimetype='application/json')

    def unsubscribe(self,version,id):
        query = {"id" : id}
        row = DbManager.query(DB_ALARM,TABLE_ALARM_SUBSCRIPTION,query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete(DB_ALARM,"alarm_subscription",id)
        return Response("", 204, mimetype='application/json')

if __name__ == '__main__':
      webserice = AlarmWebService()
      webserice.start()