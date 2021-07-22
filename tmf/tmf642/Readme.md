# TMF642 Alarm Management

 ------------------        ----------------------         ------------
| TMF642 WEBSERVICE| <--->| NO/LOW Code Adaption | <---->| Device/EMS |
 ------------------        ----------------------         ------------


 ## Fun Activities
 => Define statndard Alarm Object - Done
 
    - Alarm
    - AlarmComment
    - AlarmCrossThresholdIndicator
 
 => Define TMF probable cause - Done
 
 => Define TMF perceieved severity - Done
 
 => Define TMF Alarm type - Done
 
 => Alarm APIs End points

        Single Alarm Operation
        - Create Alarm - "/api/v1/alarm",methods='POST'
        - Modify Alarm - "/api/v1/alarm/<alarmId>",methods='PATCH'
        - Delete Alarm - "/api/v1/alarm/<alarmId>/clear", methods='POST'
        - Delete Alarm - "/api/v1/alarm/<alarmId>/delete", methods='POST'
        - Delete Alarm - "/api/v1/alarm/<alarmId>", methods='DELETE'
        - Get Alarm - "/api/v1/alarm/<alarmId>",methods='GET'

        Multiple Alarms Operations
        - Get Alarms - "/api/v1/alarms",methods='GET'
        - Ack Alarms - "/api/v1/ackAlarms",methods='POST'
        - Un Ack Alarms - "/api/v1/unAckAlarms", methods='POST'
        - Clear Alarms - "/api/v1/clearAlarms", methods='POST'
        - Comment Alarm - "/api/v1/commentsAlarms"methods='POST'
        - Group Alarm - "/api/v1/groupAlarms",methods='POST'
        - Un Group Alarm - "/api/v1/ungroupAlarms",methods='POST'
        Pub/Sub
        - Subscribe for Alarm -  "/api/v1/hub" , methods='POST'
        - unsubscribe for Alarm -  "/api/v1/hub/<id>" , methods='DELETE'
        - Publish the life cycle event to subscribed systems - <remote url>, method='POST'
        
=> Use cases

    1. Alarm Owning System -> Notified System
    
    2. Alarm Source System -> Alarm Owning System 

     

 
