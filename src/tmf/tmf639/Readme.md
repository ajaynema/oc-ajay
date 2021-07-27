# TMF639 Resource Inventory Management

 ------------------        ----------------------         ------------
| TMF639 WEBSERVICE| <--->| NO/LOW Code Adaption | <---->| Device/EMS |
 ------------------        ----------------------         ------------


 ## Fun Activities
 => Define statndard Resource Object - Done
 
    - Resource
    - PhysicalResource
    - LogicalResource
    - Equipment
    - Note
    - Place
    - ResourceAttachment
    - ResourceCharacteristic
    - ResourceParty
    - ResourceRef
    - ResourceRelationship
    - ResourceSpecification

 => Define statndard Resource Enum - Done
     - ResourceState

 => Resource Inventory APIs End points

        - Create Resource - "/tmf-api/resourceInventoryManagement/v1/resource",methods='POST'
        - Modify Resource - "/tmf-api/resourceInventoryManagement/v1/resource/<id>",methods='PATCH' 
        - Delete Resource - "/tmf-api/resourceInventoryManagement/v1/resource/<id>", methods='DELETE' 
        - Get Resource - "/tmf-api/resourceInventoryManagement/v1/resource/<id>",methods='GET' 
        - Get Resource - "/tmf-api/resourceInventoryManagement/v1/resource",methods='GET' 

        - Create Logical Resource - "/tmf-api/resourceInventoryManagement/v1/logicalResource",methods='POST'
        - Modify Logical Resource - "/tmf-api/resourceInventoryManagement/v1/logicalResource/<id>",methods='PATCH' 
        - Delete Logical Resource - "/tmf-api/resourceInventoryManagement/v1/logicalResource/<id>", methods='DELETE' 
        - Get Logical Resource - "/tmf-api/resourceInventoryManagement/v1/logicalResource/<id>",methods='GET' 
        - Get Logical Resource - "/tmf-api/resourceInventoryManagement/v1/logicalResource",methods='GET' 

        - Create Physical Resource - "/tmf-api/resourceInventoryManagement/v1/physicalResource",methods='POST'
        - Modify Physical Resource - "/tmf-api/resourceInventoryManagement/v1/physicalResource/<id>",methods='PATCH' 
        - Delete Physical Resource - "/tmf-api/resourceInventoryManagement/v1/physicalResource/<id>", methods='DELETE' 
        - Get Physical Resource - "/tmf-api/resourceInventoryManagement/v1/physicalResource/<id>",methods='GET' 
        - Get Physical Resource - "/tmf-api/resourceInventoryManagement/v1/physicalResource",methods='GET' 
       
        - Create Resource Type Resource - "/tmf-api/resourceInventoryManagement/v1/<resource_type>",methods='POST'
        - Modify Resource Type Resource - "/tmf-api/resourceInventoryManagement/v1/<resource_type>/<id>",methods='PATCH' 
        - Delete Resource Type Resource - "/tmf-api/resourceInventoryManagement/v1/<resource_type>/<id>", methods='DELETE' 
        - Get Resource Type Resource - "/tmf-api/resourceInventoryManagement/v1/<resource_type>/<id>",methods='GET' 
        - Get Resource Type Resource - "/tmf-api/resourceInventoryManagement/v1/<resource_type>",methods='GET' 
       
        Pub/Sub
        - Subscribe for Resource Notifiction -  "/tmf-api/resourceInventoryManagement/v1/hub" , methods='POST'  
        - unsubscribe for Alarm -  "/tmf-api/resourceInventoryManagement/v1/hub/<id>" , methods='DELETE' 
        - Get Subscribe for Alarm -  "/tmf-api/resourceInventoryManagement/v1/hub" , methods='GET' 
        - Publish the life cycle event to subscribed systems - <remote url>, method='POST'

=> Swagger support for APIs

=> Authentication for APIs

=> Authorization for APIs

=> Validation of the payload fields


## Q & A
Q - What is developed here ?

    TMF639 enabled web service, which manages the resource Invenory and generate events for listners.

Q - What are the resource inventory life cycle event supported?
    
Q - How to run the TMF639 Resource Inventory Web Service ?
    
    cd $SRC/tmf/tmf639
    python3 resource_inventory_web_service.py

    

 
