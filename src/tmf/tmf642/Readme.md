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

 => Define TMF Event type - Done
 
 => Alarm APIs End points

        - Create Alarm - "/tmf-api/alarmManagement/v1/alarm",methods='POST' - Done
        - Modify Alarm - "/tmf-api/alarmManagement/v1/alarm/<alarmId>",methods='PATCH' -Done
        - Delete Alarm - "/tmf-api/alarmManagement/v1/alarm/<alarmId>/clear", methods='POST' - Done
        - Delete Alarm - "/tmf-api/alarmManagement/v1/alarm/<alarmId>/delete", methods='POST' - Done
        - Delete Alarm - "/tmf-api/alarmManagement/v1/alarm/<alarmId>", methods='DELETE' - Done
        - Get Alarm - "/tmf-api/alarmManagement/v1/alarm/<alarmId>",methods='GET' - Done
        - Get Alarms - "/tmf-api/alarmManagement/v1/alarms",methods='GET' - Done
        - Ack Alarms - "/tmf-api/alarmManagement/v1/ackAlarms",methods='POST' - Done
        - Get Ack Alarms - "/tmf-api/alarmManagement/v1/ackAlarms",methods='GET' - Done
        - Get Ack Alarms - "/tmf-api/alarmManagement/v1/ackAlarms/<id>",methods='GET' - Done
        - Un Ack Alarms - "/tmf-api/alarmManagement/v1/unAckAlarms", methods='POST' - Done
        - Get Un Ack Alarms - "/tmf-api/alarmManagement/v1/unAckAlarms", methods='GET' - Done
        - Get Un Ack Alarms - "/tmf-api/alarmManagement/v1/unAckAlarms/<id>", methods='GET' - Done
        - Clear Alarms - "/tmf-api/alarmManagement/v1/clearAlarms", methods='POST' - Done
        - Get Clear Alarms - "/tmf-api/alarmManagement/v1/clearAlarms", methods='GET' - Done
        - Get Clear Alarms - "/tmf-api/alarmManagement/v1/clearAlarms/<id>", methods='GET' - Done
        - Comment Alarm - "/tmf-api/alarmManagement/v1/commentsAlarms"methods='POST' - Done
        - Get Comment Alarm - "/tmf-api/alarmManagement/v1/commentsAlarms"methods='GET' - Done
        - Get Comment Alarm - "/tmf-api/alarmManagement/v1/commentsAlarms/<id>"methods='GET' - Done
        - Group Alarm - "/tmf-api/alarmManagement/v1/groupAlarms",methods='POST' - Done
        - Get Group Alarm - "/tmf-api/alarmManagement/v1/groupAlarms",methods='GET' - Done
        - Get Group Alarm - "/tmf-api/alarmManagement/v1/groupAlarms/<id>",methods='GET' - Done
        - Un Group Alarm - "/tmf-api/alarmManagement/v1/ungroupAlarms",methods='POST' - Done
        - Get Un Group Alarm - "/tmf-api/alarmManagement/v1/ungroupAlarms",methods='GET' - Done
        - Get Un Group Alarm - "/tmf-api/alarmManagement/v1/ungroupAlarms/<id>",methods='GET' - Done
       
        Pub/Sub
        - Subscribe for Alarm -  "/tmf-api/alarmManagement/v1/hub" , methods='POST'  - Done
        - unsubscribe for Alarm -  "/tmf-api/alarmManagement/v1/hub/<id>" , methods='DELETE' - Done
        - Get Subscribe for Alarm -  "/tmf-api/alarmManagement/v1/hub" , methods='GET' - Done
        - Publish the life cycle event to subscribed systems - <remote url>, method='POST'

=> Swagger support for APIs

=> Authentication for APIs

=> Authorization for APIs

=> Use cases

    1. Alarm Owning System -> Notified System
    
    2. Alarm Source System -> Alarm Owning System 

## Q & A
Q - What is developed here ?

    TMF642 enabled web service, which manages the life cycle of alarm and generate events for listers.

Q - What are the alarm life cycle event supported?
    
    Alarm creation
    Alarm modification
    Alarm deletion
    Comment on Alarm
    Acknowledge Alarm
    Unacknowledge
    Clear the Alarm
    Subscribe for alarms related events
    Unsubscribe of alarms related events

Q - How to run the TMF642 alarm web service ?
    
    cd $SRC/tmf/tmf642
    python3 alarm_web_service.py

    

 
