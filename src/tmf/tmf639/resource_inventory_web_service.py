import sys, os.path

sys.path.append("./../../")
sys.path.append("./../")

from flask import Flask,Response,request
import jsonpickle
from db.db_manager import DbManager
from webservice.tmf_web_service import TmfWebService
import datetime

BASE_URL="/tmf-api/resourceInventoryManagement/<version>"
DB_RESOURCE_INVENTORY="DB_RESOURCE_INVENTORY"
TABLE_RESOURCE="resource"
TABLE_RESOURCE_SUBSCRIPTION="resource_inventory_event_subscription"


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
        self.register(BASE_URL+"/logicalResource","create_logical_esource",self.create_logical_esource,methods=['POST'])
        self.register(BASE_URL+"/logicalResource/<id>","modify_logical_resource",self.modify_logical_resource,methods=['PATCH'])
        #self.register(BASE_URL+"/resource/<id>","replace_resource",self.replace_resource,methods=['PUT'])
        self.register(BASE_URL+"/logicalResource/<id>","delete_logical_resource",self.delete_logical_resource,methods=['DELETE'])
        self.register(BASE_URL+"/logicalResource","get_logical_resources",self.get_logical_resources,methods=['GET'])
        self.register(BASE_URL+"/logicalResource/<id>","get_logical_resource",self.get_logical_resource,methods=['GET'])
        #Physical Resource
        self.register(BASE_URL+"/physicalResource","create_physical_esource",self.create_physical_esource,methods=['POST'])
        self.register(BASE_URL+"/physicalResource/<id>","modify_physical_resource",self.modify_physical_resource,methods=['PATCH'])
        #self.register(BASE_URL+"/resource/<id>","replace_resource",self.replace_resource,methods=['PUT'])
        self.register(BASE_URL+"/physicalResource/<id>","delete_physical_resource",self.delete_physical_resource,methods=['DELETE'])
        self.register(BASE_URL+"/physicalResource","get_physical_resources",self.get_physical_resources,methods=['GET'])
        self.register(BASE_URL+"/physicalResource/<id>","get_physical_resource",self.get_physical_resource,methods=['GET'])

    
    def get_resource(self,version,id):
        return self.get_by_id(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)

    def get_resources(self,version):
        return self.get_all(DB_RESOURCE_INVENTORY,TABLE_RESOURCE)
    
    def create_resource(self,version):
        data = request.get_json()
        row = DbManager.insert(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,data)
        #self.create_event(EventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def modify_resource(self,version,id):
       data = request.get_json()
      # self.create_event(EventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id,data)

    def delete_resource(self,version,id):
        query = {"id" : id}
        row = DbManager.query(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)
       # self.create_event(EventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')

    def get_logical_resource(self,version,id):
        return self.get_by_id(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)

    def get_logical_resources(self,version):
        return self.get_all(DB_RESOURCE_INVENTORY,TABLE_RESOURCE)
    
    def create_logical_resource(self,version):
        data = request.get_json()
        row = DbManager.insert(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,data)
        #self.create_event(EventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def modify_logical_resource(self,version,id):
       data = request.get_json()
      # self.create_event(EventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id,data)

    def delete_logical_resource(self,version,id):
        query = {"id" : id}
        row = DbManager.query(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)
       # self.create_event(EventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')

    def get_physical_resource(self,version,id):
        return self.get_by_id(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)

    def get_physical_resources(self,version):
        return self.get_all(DB_RESOURCE_INVENTORY,TABLE_RESOURCE)
    
    def create_physical_resource(self,version):
        data = request.get_json()
        row = DbManager.insert(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,data)
        #self.create_event(EventType.AlarmCreateEvent,data)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def modify_physical_resource(self,version,id):
       data = request.get_json()
      # self.create_event(EventType.AlarmAttributeValueChangeEvent,data)
       return self.patch(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id,data)

    def delete_physical_resource(self,version,id):
        query = {"id" : id}
        row = DbManager.query(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,query)
        if (row is None):
            return Response("", 404 ,mimetype='application/json')
        DbManager.delete(DB_RESOURCE_INVENTORY,TABLE_RESOURCE,id)
       # self.create_event(EventType.AlarmDeleteEvent,row)
        return Response("", 204, mimetype='application/json')
