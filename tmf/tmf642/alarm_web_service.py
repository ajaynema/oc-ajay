from flask import Flask,Response,request
import jsonpickle
from json import JSONEncoder
import json

class AlarmWebService:
    def __init__(self,name):
        self.name = name
        self.api = Flask(self.name)
        self.api.add_url_rule("/<resource_name>","get",self.get,methods=['GET'])
        self.api.add_url_rule("/<resource_name>/<id>","get_by_id",self.getById,methods=['GET'])
        self.api.add_url_rule("/<resource_name>","add",self.add,methods=['POST'])
        self.api.add_url_rule("/<resource_name>/<id>","modify",self.modify,methods=['POST'])
        self.api.add_url_rule("/<resource_name>/<id>/<action>","action",self.action,methods=['POST'])
        self.api.add_url_rule("/<resource_name>/<id>/<action>","action",self.action,methods=['GET'])
        self.api.add_url_rule("/<resource_name>/<id>","delete",self.delete,methods=['DELETE'])

    def get(self,resource_name):
        return Response("", 200,mimetype='application/json')
  
    def getById(self,resource_name,id):
        result = {}
        return Response("", 200,mimetype='application/json')
    
    def add(self,resource_name):
        result = {}
        resource = self.resourceManager.get(resource_name)
        if (resource is None):
            result['code'] = 405
            result['message'] = "METHOD-NOT-ALLOWED"
            response_str = jsonpickle.encode(result)
            return Response(response_str, 405)
        print("add -> " + resource_name)
        data = request.get_json()
        dbContext = DBContext(resource)
        resultResource = DBManager.insert(dbContext,data)
        result = {}
        result['code'] = 0
        result['message'] = 0
        result['resource'] = resultResource
        response_str = jsonpickle.encode(result)
        return Response(response_str, 200,mimetype='application/json')

    def modify(self,resource_name,id):
        result = {}
        resource = self.resourceManager.get(resource_name)
        if (resource is None):
            result['code'] = 405
            result['message'] = "METHOD-NOT-ALLOWED"
            response_str = jsonpickle.encode(result)
            return Response(response_str, 405)
        print("Modify ID -> " + resource_name + ",ID="+id)
        resource = self.resourceManager.get(resource_name)
        if (resource is None):
            result['code'] = 405
            result['message'] = "METHOD-NOT-ALLOWED"
            response_str = jsonpickle.encode(result)
            return Response(response_str, 405)
        print("add -> " + resource_name)
        data = request.get_json()
        dbContext = DBContext(resource)
        resultResource = DBManager.update(dbContext,id,data)   
        result['code'] = 0
        result['message'] = 0
        result['resource'] = resultResource
        response_str = jsonpickle.encode(result)
        return Response(response_str, 200,mimetype='application/json')
  
    def delete(self,resource_name,id):
        print("Delete  -> " + resource_name + ", ID="+id)
        result = {}
        resource = self.resourceManager.get(resource_name)
        if (resource is None):
            result['code'] = 405
            result['message'] = "METHOD-NOT-ALLOWED"
            response_str = jsonpickle.encode(result)
            return Response(response_str, 405)
        
        dbContext = DBContext(resource)
        resultResource = DBManager.delete(dbContext,id)
        result['code'] = 0
        result['message'] = 0
        result['resource'] = resultResource
        response_str = jsonpickle.encode(result)
        return Response(response_str, 200,mimetype='application/json')
    
    def action(self,resource_name,id,action):
        result = {}
        resource = self.resourceManager.get(resource_name)
        if (resource is None):
            result['code'] = 405
            result['message'] = "METHOD-NOT-ALLOWED"
            response_str = jsonpickle.encode(result)
            return Response(response_str, 405)
        print("Action -> " + resource_name + ", ID="+id + ", Action="+action)
        return Response('success', 200,mimetype='application/json')


    def start(self):
        self.api.run()
