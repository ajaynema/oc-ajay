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
        - Create Alarm - "/alarm",methods='POST'
        - Modify Alarm - "/alarm/<alarmId>",methods='PATCH'
        - Delete/Clear Alarm - "/alarm/<alarmId>/clear", methods='POST'
        - Get Alarm - "/alarm/<alarmId>",methods='GET'

        Multiple Alarms Operations
        - Get Alarms - "/alarms",methods='GET'
        - Ack Alarms - "/ackAlarms",methods='POST'
        - Un Ack Alarms - "/unAckAlarms", methods='POST'
        - Clear Alarms - "/clearAlarms", methods='POST'
        - Comment Alarm - "/commentsAlarms"methods='POST'
        - Group Alarm - "/groupAlarms",methods='POST'
        - Un Group Alarm - "/ungroupAlarms",methods='POST'
     

 