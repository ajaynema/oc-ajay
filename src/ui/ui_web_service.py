import sys, os.path
import datetime
sys.path.append("./../../")

from flask import Flask,Response,request
import jsonpickle
from ui_from_yang_json import UIFromYANGJson

class UIWebService:
    def __init__(self,name="WebService",host="0.0.0.0",port=80):
        self.name = name
        self.port = port
        self.host = host
        self.api = Flask(self.name)
        self.register("/ui/yang/<json>","yang_ui",self.yang_ui,methods=['GET'])
        self.register("/ui/yang/<json>/<path:path>","yang_ui_path",self.yang_ui_path,methods=['GET'])
        
    def register(self, url,func,func_pointer,methods=['GET']):
        self.api.add_url_rule(url,func,func_pointer,methods=methods)

    def yang_ui_path(self,json,path="/"):
         return self.yang_ui(json, path="/"+path)

    def yang_ui(self,json,path="/"):
        uiFromYANGJson =  UIFromYANGJson(jsonfile=json)
        response_str  = uiFromYANGJson.getView(path=path)
        return Response(response_str, 200, mimetype='text/html; charset=UTF-8')

    def start(self):
        self.api.run(host=self.host,port=self.port)

if __name__ == '__main__':
      webserice = UIWebService()
      webserice.start()