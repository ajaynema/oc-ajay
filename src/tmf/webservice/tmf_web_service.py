import sys, os.path

sys.path.append("./../../")

from flask import Flask,Response,request
import jsonpickle
from db.db_manager import DbManager

class TmfWebService:
    def __init__(self,name="WebService",port=80):
        self.name = name
        self.port = port
        self.api = Flask(self.name)
    
    def register(self, url,func,func_pointer,methods=['GET']):
        self.api.add_url_rule(url,func,func_pointer,methods=methods)
    
    def start(self):
        self.api.run(host="0.0.0.0",port=self.port)
    
    def get_all(self, database,table):
        fields = request.args.get("fields") if (request.args.get("fields") is not None) else None
        offset = int(request.args.get("offset")) if (request.args.get("offset") is not None) else None
        limit = int(request.args.get("limit")) if (request.args.get("limit") is not None) else None
        row = DbManager.get_all(database,table,fields=fields,offset=offset,limit=limit)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
    def get_by_id(self,database,table,id):
        fields = request.args.get("fields")
        query = {"id" : id}
        row = DbManager.query(database,table,query,fields)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def get_field_from_path(self,path):
        if path.startswith("/"):
            path = path[1:]
        path = path.replace('/','.')
        return path

    def patch(self, database, table, id, patch_data):
        for row in patch_data:
            if (row['op'] == "replace"):
               path = row['path']
               field_name = self.get_field_from_path(path)
               value = row['value']
               change_data = {}
               change_data[field_name] = value
               print(change_data)
               DbManager.update(database,table,id,change_data)  
            elif row['op'] == "add":
               path = row['path']
               field_name = self.get_field_from_path(path)
               value = row['value']
               change_data = {}
               change_data[field_name] = value
               DbManager.update(database,table,id,change_data) 
            elif row['op'] == "remove":
               path = row['path']
               field_name = self.get_field_from_path(path)
               DbManager.delete_field(database,table,id,field_name)      
        return Response("", 200, mimetype='application/json')
 