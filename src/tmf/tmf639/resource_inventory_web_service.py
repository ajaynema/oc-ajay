import sys, os.path

sys.path.append("./../../")
sys.path.append("./../")

from flask import Flask,Response,request
import jsonpickle
from db.db_manager import DbManager
from webservice.tmf_web_service import TmfWebService
import datetime
from resource_table_helper import ResourceTableHelper

BASE_URL="/tmf-api/resourceInventoryManagement/<version>"



class ResourceInventoryWebService(TmfWebService):
    def __init__(self,name="ResourceInventoryWebService",port=80):
        super().__init__(name=name,port=port)
        
        self.register(BASE_URL+"/resource","create_resource",self.create_resource,methods=['POST'])
        self.register(BASE_URL+"/resource/<id>","modify_resource",self.modify_resource,methods=['PATCH'])
        #self.register(BASE_URL+"/resource/<id>","replace_resource",self.replace_resource,methods=['PUT'])
        self.register(BASE_URL+"/resource/<id>","delete_resource",self.delete_resource,methods=['DELETE'])
        self.register(BASE_URL+"/resource","get_resources",self.get_resources,methods=['GET'])
        self.register(BASE_URL+"/resource/<id>","get_resource",self.get_resource,methods=['GET'])
        #Logical Resource
        self.register(BASE_URL+"/logicalResource","create_logical_resource",self.create_logical_resource,methods=['POST'])
        self.register(BASE_URL+"/logicalResource/<id>","modify_logical_resource",self.modify_logical_resource,methods=['PATCH'])
        #self.register(BASE_URL+"/resource/<id>","replace_resource",self.replace_resource,methods=['PUT'])
        self.register(BASE_URL+"/logicalResource/<id>","delete_logical_resource",self.delete_logical_resource,methods=['DELETE'])
        self.register(BASE_URL+"/logicalResource","get_logical_resources",self.get_logical_resources,methods=['GET'])
        self.register(BASE_URL+"/logicalResource/<id>","get_logical_resource",self.get_logical_resource,methods=['GET'])
        #Physical Resource
        self.register(BASE_URL+"/physicalResource","create_physical_resource",self.create_physical_resource,methods=['POST'])
        self.register(BASE_URL+"/physicalResource/<id>","modify_physical_resource",self.modify_physical_resource,methods=['PATCH'])
        #self.register(BASE_URL+"/resource/<id>","replace_resource",self.replace_resource,methods=['PUT'])
        self.register(BASE_URL+"/physicalResource/<id>","delete_physical_resource",self.delete_physical_resource,methods=['DELETE'])
        self.register(BASE_URL+"/physicalResource","get_physical_resources",self.get_physical_resources,methods=['GET'])
        self.register(BASE_URL+"/physicalResource/<id>","get_physical_resource",self.get_physical_resource,methods=['GET'])
        
         #Resource Type
        self.register(BASE_URL+"/<resource_type>","create_resource_type_resource",self.create_resource_type_resource,methods=['POST'])
        self.register(BASE_URL+"/<resource_type>/<id>","modify_resource_type_resource",self.modify_physical_resource,methods=['PATCH'])
        #self.register(BASE_URL+"/resource/<id>","replace_resource",self.replace_resource,methods=['PUT'])
        self.register(BASE_URL+"/<resource_type>/<id>","delete_resource_type_resource",self.delete_resource_type_resource,methods=['DELETE'])
        self.register(BASE_URL+"/<resource_type>","get_resource_type_resources",self.get_resource_type_resources,methods=['GET'])
        self.register(BASE_URL+"/<resource_type>/<id>","get_resource_type_resource",self.get_resource_type_resource,methods=['GET'])
        self.register(BASE_URL+"/hub","subscribe",self.subscribe,methods=['POST'])      
        self.register(BASE_URL+"/hub","get_subscribe",self.get_subscribe,methods=['GET'])
        self.register(BASE_URL+"/hub/<id>","unsubscribe",self.unsubscribe,methods=['DELETE'])

     def create_event(self,eventType,event_data):
        event = {}
        event['eventType']  = eventType.name
        event['event'] = event_data
        event['eventTime'] = self.get_formated_time()
        event['status'] = "pending"
        DbManager.insert(DB_RESOURCE_INVENTORY,TABLE_RESOURCE_INVENTORY_EVENT,event)

    def get_resource(self,version,id):
        return self.get_by_id(ResourceTableHelper(),id)

    def get_resources(self,version):
        return self.get_all(ResourceTableHelper())
    
    def create_resource(self,version):
        data = request.get_json()
        row = ResourceTableHelper().insert(data)
        #self.create_event(EventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def modify_resource(self,version,id):
       data = request.get_json()
      # self.create_event(EventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(ResourceTableHelper(),id,data)

    def delete_resource(self,version,id):
        query = {"id" : id}
        row = ResourceTableHelper().get_by_id(id)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        ResourceTableHelper().delete(id)
       # self.create_event(EventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')

    def get_logical_resource(self,version,id):
        return self.get_by_id(ResourceTableHelper(),id)

    def get_logical_resources(self,version):
        return self.get_all(ResourceTableHelper())
    
    def create_logical_resource(self,version):
        data = request.get_json()
        row = DbManager.insert(ResourceTableHelper(),data)
        #self.create_event(EventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def modify_logical_resource(self,version,id):
       data = request.get_json()
      # self.create_event(EventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(ResourceTableHelper(),id,data)

    def delete_logical_resource(self,version,id):
        row = ResourceTableHelper().get_by_id(id)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        ResourceTableHelper().delete(id)
       # self.create_event(EventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')

    def get_physical_resource(self,version,id):
        return self.get_by_id(ResourceTableHelper(),id)

    def get_physical_resources(self,version):
        return self.get_all(ResourceTableHelper())
    
    def create_physical_resource(self,version):
        data = request.get_json()
        row = ResourceTableHelper().insert(data)
        #self.create_event(EventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def modify_physical_resource(self,version,id):
       data = request.get_json()
      # self.create_event(EventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(ResourceTableHelper(),id,data)

    def delete_physical_resource(self,version,id):
        row = ResourceTableHelper().get_by_id(id)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        ResourceTableHelper().delete(id)
       # self.create_event(EventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')

    def get_resource_type_resource(self,version,resource_type,id):
        return self.get_by_id(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)

    def get_resource_type_resources(self,version):
        return self.get_all(DB_RESOURCE_INVENTORY,TABLE_RESOURCE)
    
    def create_resource_type_resource(self,version,resource_type):
        data = request.get_json()
        row = DbManager.insert(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,data)
        #self.create_event(EventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def modify_resource_type_resource(self,version,resource_type,id):
       data = request.get_json()
      # self.create_event(EventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id,data)

    def delete_resource_type_resource(self,version,resource_type,id):
        query = {"id" : id}
        row = DbManager.query(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)
       # self.create_event(EventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')
    
    def subscribe(self,version):
        data = request.get_json()
        callback = data['callback']
        query = {"callback" : callback}
        row = DbManager.query(DB_RESOURCE_INVENTORY,TABLE_RESOURCE_INVENTORY_EVENT_SUBSCRIPTION,query)
        if (row is not None):
            return Response("", 409 ,mimetype='application/json')
        row = DbManager.insert(DB_ALARM,TABLE_RESOURCE_INVENTORY_EVENT_SUBSCRIPTION,data)
        result={}
        result['id'] = row['id']
        result['callback'] = row['callback']
        response_str = jsonpickle.encode(result)
        print(response_str)
        return Response(response_str, 200, mimetype='application/json')

    def unsubscribe(self,version,id):
        query = {"id" : id}
        row = DbManager.query(DB_RESOURCE_INVENTORY,TABLE_RESOURCE_INVENTORY_EVENT_SUBSCRIPTION,query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete(DB_RESOURCE_INVENTORY,TABLE_RESOURCE_INVENTORY_EVENT_SUBSCRIPTION,id)
        return Response("", 204, mimetype='application/json')

if __name__ == '__main__':
      webserice = ResourceInventoryWebService()
      webserice.start()