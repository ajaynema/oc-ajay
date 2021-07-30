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
            other_ui_objects={}
            fields=[]
            subtree = array_object[1]
            for key in subtree:
                 #print(key)
                 ui_object ={}
                 sub_tree_object = subtree[key]
                 parent_object['type'] = "list"
                 ui_object['type'] = "block"
                 self.getUICompoment(ui_object,sub_tree_object)
                 ui_object['key'] = key
                 if (key == "config"):
                    ui_object['type'] = "block" 
                    parent_object['config_tree'] = ui_object
                 elif (key == "state"):
                    ui_object['type'] = "block"  
                    parent_object['state_tree'] = ui_object
                 else:
                    #print(ui_object['key']) 
                    if (ui_object['type'] == "field"):
                        fields.append(ui_object)
                    else:
                        other_ui_objects[ui_object['key']] = ui_object
            if (len(other_ui_objects) > 0):
                parent_object['other_tree'] = other_ui_objects        
            if (len(fields) > 0):
                parent_object['fields'] = fields
            if len(array_object) > 0:
                if len(array_object[2]) > 0:
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
        print(tokens)
        for token in tokens:
            if token == "" :
                return_ui_data = ui_data
            else :
                if 'other_tree' in return_ui_data:
                    return_ui_data = return_ui_data['other_tree']
                    return_ui_data = return_ui_data[token]

        return return_ui_data
    
    def isForm(self, op=None):
        if (op is None):
            return False
        if (op=="add"):
            return True
        if (op=="edit"):
            return True
        if (op=="create"):
            return True
        if (op=="modify"):
            return True
        return False
            
    def getHtmlFromPathObject(self, ui_data,data=None,indent=1,op=None,parent_path="/"):
        indent_str =""
        html = "<html>\n"
        html = html + '''
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <!-- Font Awesome -->
            <link
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"
            rel="stylesheet"
            />
            <!-- Google Fonts -->
            <link
            href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
            rel="stylesheet"
            />
            <!-- MDB -->
            <link
            href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.6.0/mdb.min.css"
            rel="stylesheet"
            />
            <!-- MDB -->
            <script
            type="text/javascript"
            src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.6.0/mdb.min.js"
            ></script>
        
        '''
        html = html+"<body>\n"
        html = html+'''
        <div>
        <div>
          <nav class="navbar navbar-expand-lg navbar-light bg-light navbar-fixed-top" style="padding-left:0px;background-color:silver!important">
            <div class="container-fluid no-padding-xs" style="width:100%;">
              <div class="navbar-header">
                	<button style="float:left; margin-left:10px" class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
                <a class="navbar-brand" style="padding-top:2px;padding-left:35px">                  
                 Open Config - UI
                </a>
              </div> 
              <div id="navbar" class="collapse navbar-collapse justify-content-end">
                <ul class="nav navbar-nav navbar-right text-right ms-auto mb-2 mb-lg-0">
                  <li id="" class="nav-item" >
                    <a style="padding-top:13px;color:black;text-decoration: none;margin-left:30px;" href="/ui/yang/network-instances">Network Instance</a>
                  </li> 
                  <li id="" class="nav-item" >
                    <a style="padding-top:13px;color:black;text-decoration: none;margin-left:30px;" href="/ui/yang/platform">Platform</a>
                  </li> 
                  <li id="" class="nav-item" >
                    <a style="color:black;text-decoration: none;margin-left: 30px;margin-right: 30px;" href="/ui/yang/system">System</a>
                  </li> 
                </ul> 
              </div> 
            </div> 
          </nav> 
        </div> 
      </div>
      '''
        html = html+"<div class=\"container-fluid\">"
        html = html+"<div class=\"row\" style=\"margin-top:10px;\">"
        html = html+'''<div class="col-lg-3 col-md-3 col-md-left">'''
        if ("other_tree" in ui_data):
            html = html+'''
            <div class="font-18 text-center no-margin text-gray-black padding-b-5"           style="background-color:#00BCD4;padding:6px;color:white;">'''
            html = html+self.jsonfile
            html = html+"</div>"
            other_tree = ui_data['other_tree']
            html = html+'''
            <div class="box-body no-padding">'''
            for key in other_tree:
                other = other_tree[key]
                print(parent_path)
                path_seperator="/"
                if (op is None):
                    op="list"
                if (parent_path == "/"):
                    path_seperator=""
                if (other['type'] == "list"):
                    html = html + indent_str+ "<a class=\"list-group-item with_indentation with_icon \" href=\"/ui/yang/"+self.jsonfile+parent_path+path_seperator+key+"\">"+key+" list<a>\n"
                else:   
                    html = html + indent_str+ "<a class=\"list-group-item with_indentation with_icon \" href=\"/ui/yang/"+self.jsonfile+parent_path+path_seperator+key+"?op="+op+"\">"+key+"<a>\n" 
            html = html+'</div>'
        html = html+"</div>"
        html = html+'''<div class="col-lg-9 col-md-9 col-sm-12 col-md-center-and-right">'''
        draw_view = None
        html = html+'''<div style="margin:30px;width:90%;">'''
        for i in range(0, indent):
            indent_str += ' '
        if "state_tree" in ui_data:
            if (self.isForm(op)):
                draw_view = ui_data['config_tree']
                html = html +'''
                <div>
                  <h4 class="font-18 text-center no-margin text-gray-black padding-b-5"     style="background-color:#00BCD4;padding:6px;color:white;">
                        Config view
                  </h4> 
                </div> 
                <div class="clearfix">
                </div> '''
            else :
                draw_view = ui_data['state_tree']
                html = html +'''
                <div>
                  <h4 class="font-18 text-center no-margin text-gray-black padding-b-5"     style="background-color:#00BCD4;padding:6px;color:white;">
                        State view
                  </h4> 
                </div> 
                <div class="clearfix">
                </div> '''  
            if "fields" in draw_view :
                html = html + indent_str+ "<form class=\"flat_form form-horizontal\">\n"
                html = html + indent_str+ "<table class=\"form_table\" cellspacing=\"4\" cellpadding=\"4\" style=\"width:100%\">\n"
                for field in draw_view['fields']:
                    value = ""
                    readonly=""
                    if ((data is not None) and  (field['key'] in data)) :
                        value =  str(data[field['key']])
                    if (self.isForm(op)):
                        readonly="readonly"
                    html = html + indent_str+"   "+"<tr><td class=\"col-sm-4\">"+ field['key'] + "</td><td class=\"col-sm-8\"><input type=\"text\" id=\""+field['key']+"\" name=\""+field['key']+"\" value=\""+value+"\" class=\"form-control\" "+readonly+"></input></td></tr>\n"
                html = html + indent_str+ "</table>\n"

                if (self.isForm(op)):
                    html = html + '''<div class="form_footer " style="width:100%; padding: 5px; background-color: #DCDCDC;" align="right">
                        <a href="/ui/meter_category" style="color:#C8C8C8;">                      <input id="cancel" type="button" style="width:100px;padding-top:5px;padding-bottom:5px;" value="Cancel" /> 
    </a>
                        <input id="save" class="form_buttonbtn btn-success" type="submit" style="margin-left:20px;width:100px;padding-top:5px;padding-bottom:5px;" value="Save" /> 
                    </div>'''
                else :
                    html = html + '''<div class="form_footer " style="width:100%; padding: 5px; background-color: #DCDCDC;" align="right">
                        <input id="save" class="form_buttonbtn btn-success" type="submit" style="margin-left:20px;width:100px;padding-top:5px;padding-bottom:5px;" value="Edit" /> 
                    </div>'''    
                html = html + indent_str+ "</form>\n"
        html = html+"</div>"
        html = html+"</div>"
        html = html+"</div>"
        html = html+"</div>"
        html = html+"</body>\n"
        html = html+ "</html>\n"
        return html

    def getHtml(self, ui_data, data=None, parent_path="/",indent=1,op=None):
        if parent_path == "/":
            _ui_data = ui_data
        else:    
            _ui_data = self.getUIDataFromPath(ui_data,parent_path)
        data = self.getTestData(parent_path)
        html = self.getHtmlFromPathObject(_ui_data,data=data,indent=indent,op=op,parent_path=parent_path)
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

    def getView(self, path="/",op=None):
        json_data = self.loadJson()
        ui_data = self.json2UI(json_data)
        data = {}
        view = self.getHtml(ui_data,data,parent_path=path,op=op)
        return view
       # print(view)
        
if __name__ == '__main__':
      uiFromYANGJson = UIFromYANGJson(jsonfile="network-instances")
      #view = uiFromYANGJson.getView(path="/network-instance")
      #print(view)
      json_data = uiFromYANGJson.loadJson()
      ui_data = uiFromYANGJson.json2UI(json_data)
     # uiFromYANGJson.getUIDataFromPath(ui_data,"/dns")
      print(json.dumps(ui_data))
