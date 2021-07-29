import json

class UIFromYANGJson:
    def __init__(self, jsonpath="./json/openconfig",jsonfile=None):
        self.jsonpath = jsonpath
        self.jsonfile = jsonfile
    
    def getRootObject(self,tree):
        root_object = None
        for key in tree:
            root_object = tree[key]
        return root_object

    def getRootKey(self,tree):
        key = None
        for key in tree:
            key = key
        return key

    def getUICompoment(self,parent_object,array_object):
        #print(array_object)
        #print("\n\n")
        if (array_object is None):
            return
        type = array_object[0]
        
        if (type == "container"):
            other_ui_objects={}
            fields=[]
            subtree = array_object[1]
            for key in subtree:
                 ui_object ={}
                 sub_tree_object = subtree[key]
                 ui_object['type'] = "block"
                 self.getUICompoment(ui_object, sub_tree_object)
                 ui_object['key'] = key
                 if (key == "config"):
                     parent_object['config_tree'] = ui_object
                 elif (key == "state"):
                     parent_object['state_tree'] = ui_object
                 else:
                    if (ui_object['type'] == "field"):
                        fields.append(ui_object)
                    else:
                        other_ui_objects[ui_object['key']] = ui_object
            if (len(other_ui_objects) > 0):
                parent_object['other_tree'] = other_ui_objects
            if (len(fields) > 0):
                parent_object['fields'] = fields
        elif (type == "list"):
            other_ui_objects=[]
            subtree = array_object[1]
            for key in subtree:
                 ui_object ={}
                 sub_tree_object = subtree[key]
                 parent_object['type'] = "list"
                 self.getUICompoment(ui_object,sub_tree_object)
                 ui_object['key'] = key
                 if (key == "config"):
                    ui_object['type'] = "block" 
                    parent_object['config_tree'] = ui_object
                 elif (key == "state"):
                    ui_object['type'] = "block"  
                    parent_object['state_tree'] = ui_object
                 else:
                    other_ui_objects.append(ui_object)
            
            key_tree = array_object[2][0]
            key_field = key_tree[1]
            parent_object['key_field'] = key_field
                

        elif (type == "leaf"):
            subtree = array_object[1]
           # ui_object ={}
            parent_object['value_type'] = array_object[1]
            parent_object['type'] = "field"
            return
            # ui_objects.append(ui_object)         
        
        return

    def loadJson(self):
        f = open(self.jsonpath+"/"+self.jsonfile+".json")
        json_data = json.load(f)
        return json_data

    def json2UI(self,json_data):    
        tree = json_data['tree']
        root_object =  self.getRootObject(tree)
        ui_data = {}
        ui_data['type'] = "block"
        ui_data['key'] = "root"
        self.getUICompoment(ui_data,root_object)
        return ui_data

    def getUIDataFromPath(self,ui_data,path):
        tokens = path.split("/")
        return_ui_data = None
        for token in tokens:
            if token == "" :
                return_ui_data = ui_data
            else :
                if 'other_tree' in return_ui_data:
                    return_ui_data = return_ui_data['other_tree']
                    return_ui_data = return_ui_data[token]

        return return_ui_data

    def getHtmlFromPathObject(self, ui_data, data=None,indent=1):
        indent_str =""
        html = "<html>\n"
        html = html+"<body>\n"
        draw_view = None
        for i in range(0, indent):
            indent_str += ' '
        if "state_tree" in ui_data:
            draw_view = ui_data['state_tree']
            html = html + indent_str+ "<h2>state view<h2>\n"
            if "fields" in draw_view :
                html = html + indent_str+ "<table>\n"
                for field in draw_view['fields']:
                    value = "-"
                    if ((data is not None) and  (field['key'] in data)) :
                        value =  str(data[field['key']])
                    html = html + indent_str+"   "+"<tr><td>"+ field['key'] + "</td><td>"+value+"</td></tr>\n"
                html = html + indent_str+ "</table>\n"
        if ("other_tree" in ui_data):
            other_tree = ui_data['other_tree']
            for key in other_tree:
                other = other_tree[key]
                if (other['type'] == "list"):
                    html = html + indent_str+ "<a>"+key+" list<a>\n"
                else:    
                    html = html + indent_str+ "<a>"+key+"<a>\n"
        html = html+"</body>\n"
        html = html+ "</html>\n"
        return html

    def getHtml(self, ui_data, data=None, parent_path="/",indent=1):
        if parent_path == "/":
            _ui_data = ui_data
        else:    
            _ui_data = self.getUIDataFromPath(ui_data,parent_path)
        data = self.getTestData(parent_path)
        html = self.getHtmlFromPathObject(_ui_data,data=data,indent=indent)
        return html

    def getTestData(self,data_type="/"):
        if data_type=="/":
            data = {}
            data['hostname'] = "test-hostname"
            return data
        elif (data_type == "/memory"):
            data = {}
            data['physical'] = 200
            data['reserved'] = 250
            return data
        elif (data_type == "/aaa"):
            data = {}
            data['enable'] = True
            return data
        return None

    def getView(self, path="/"):
        json_data = self.loadJson()
        ui_data = self.json2UI(json_data)
        data = {}
        view = self.getHtml(ui_data,data,parent_path=path)
        return view
       # print(view)
        
if __name__ == '__main__':
      uiFromYANGJson = UIFromYANGJson(jsonfile="system")
      view = uiFromYANGJson.getView(path="/memory")
      print(view)
     # json_data = uiFromYANGJson.loadJson()
     # ui_data = uiFromYANGJson.json2UI(json_data)
     # uiFromYANGJson.getUIDataFromPath(ui_data,"/dns")
      #print(json.dumps(ui_data))
