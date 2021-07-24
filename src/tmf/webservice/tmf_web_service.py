import sys, os.path

sys.path.append("./../../")

from flask import Flask,Response,request
import jsonpickle
from db.db_manager import DbManager

class TmfWebService:
    def __init__(self,name="WebService",port=80):
        self.name = name
        self.api = Flask(self.name)
    
    def register(self, url,func,func_pointer,methods=['GET']):
        self.api.add_url_rule(url,func,func_pointer,methods=methods)
    
    def start():
        self.api.start()
    
    def get_all(self, database,table):
        fields = request.args.get("fields") if (request.args.get("fields") is not None) else None
        offset = int(request.args.get("offset")) if (request.args.get("offset") is not None) else None
        limit = int(request.args.get("limit")) if (request.args.get("limit") is not None) else None
        row = DbManager.get_all(database,table,fields=fields,offset=offset,limit=limit)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
