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
            other_ui_objects=[]
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
                        other_ui_objects.append(ui_object)
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
        f = open(self.jsonpath+"/"+self.jsonfile)
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

    def getView(self, path=None):
        json_data = self.loadJson()
        ui_data = self.json2UI(json_data)
        print(json.dumps(ui_data, indent = 3))

if __name__ == '__main__':
      uiFromYANGJson = UIFromYANGJson(jsonfile="system.json")
      uiFromYANGJson.getView()