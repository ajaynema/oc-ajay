#TMF642 Alarm Management

 ------------------        ----------------------         ------------
| TMF642 WEBSERVICE| <--->| NO/LOW Code Adaption | <---->| Device/EMS |
 ------------------        ----------------------         ------------


 ##Fun Activities
 => Define statndard Alarm Object - Done
    - Alarm
    - AlarmComment
    - AlarmCrossThresholdIndicator
 => Define TMF probable cause - Done
 => Define TMF perceieved severity - Done
 => Define TMF Alarm type - Done
 => Alarm APIs End points

        Single Alarm Operation
        - Create Alarm - "/api/alarm",methods='POST'
        - Modify Alarm - "/api/alarm/<alarmId>",methods='PATCH'
        - Delete Alarm - "/api/alarm/<alarmId>/clear", methods='POST'
        - Delete Alarm - "/api/alarm/<alarmId>/delete", methods='POST'
        - Delete Alarm - "/api/alarm/<alarmId>", methods='DELETE'
        - Get Alarm - "/api/alarm/<alarmId>",methods='GET'

        Multiple Alarms Operations
        - Get Alarms - "/api/alarms",methods='GET'
        - Ack Alarms - "/api/ackAlarms",methods='POST'
        - Un Ack Alarms - "/api/unAckAlarms", methods='POST'
        - Clear Alarms - "/api/clearAlarms", methods='POST'
        - Comment Alarm - "/api/commentsAlarms"methods='POST'
        - Group Alarm - "/api/groupAlarms",methods='POST'
        - Un Group Alarm - "/api/ungroupAlarms",methods='POST'
        Pub/Sub
        - Subscribe for Alarm -  "/api/hub" , methods='POST'
        - unsubscribe for Alarm -  "/api/hub/<id>" , methods='DELETE'
        - Publish the life cycle event to subscribed systems - <remote url>, method='POST'
        
=> Use cases
    1. Alarm Owning System -> Notified System
    2. Alarm Source System -> Alarm Owning System 

     

 