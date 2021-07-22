from alarm_type import AlarmType
from alarm_probable_cause import AlarmProbableCause
from alarm_perceived_severity import AlarmPerceivedSeverity
class Alarm:
    def __init__(self):
        self.id = ""
        self.href = ""
        self.baseType = ""
        self.type = ""
        self.schemaLocation = ""
        self.externalAlarmId = ""
        self.state = ""
        self.alarmType = AlarmType.unkownn
        self.perceivedSeverity = AlarmPerceivedSeverity.indeterminate
        self.probableCause = AlarmProbableCause.other
        
        self.specificProblem = ""
        self.specificProblem = ""
        
        self.alarmedObject = {}
        self.alarmedObjectType = ""

        self.sourceSystemId = ""
        self.alarmDetails = ""
        self.alarmEscalation = False
        self.serviceAffecting = False
        self.reportingSystemId=""
        
        #times
        self.alarmRaisedTime = ""
        self.alarmReportingTime = ""
        self.alarmChangedTime = ""
        
        #clear
        self.alarmClearedTime = ""
        self.clearSystemId=""
        self.clearUserId=""
        
        #ack
        self.ackSystemId = ""
        self.ackUserId = ""
        self.ackTime = ""
        self.ackState = ""
        self.crossedThresholdInformation = {}
        
        self.isRoot = ""
        self.isRootCause =False #A boolean. Indicates whether the alarm is a root cause alarm.
        self.plannedOutageIndicator =""
        self.proposedRepairedActions=""

        self.place = []
        self.parentAlarm = []
        self.correlatedAlarm = []
        self.comment = []
        self.affectedService = []
       


    def getId(self):
        return self.id

    def setId(self,value):
         self.id = value

    def getHref(self):
        return self.href

    def setHref(self,value):
         self.href = value

    def getBaseType(self):
        return self.baseType

    def setBaseType(self,value):
         self.baseType = value

    
    def getType(self):
        return self.type

    def setType(self,value):
         self.type = value

    def getSchemaLocation(self):
        return self.schemaLocation

    def setSchemaLocation(self,value):
         self.schemaLocation = value

    def getExternalAlarmId(self):
        return self.externalAlarmId

    def setExternalAlarmId(self,value):
         self.externalAlarmId = value

    def getState(self):
        return self.state

    def setState(self,value):
         self.state = value

    def getAlarmType(self):
        return self.alarmType

    def setAlarmType(self,value):
         self.alarmType = value    
        
    def getPerceivedSeverity(self):
        return self.perceivedSeverity

    def setPerceivedSeverity(self,value):
         self.perceivedSeverity = value   
    
    def getProbableCause(self):
        return self.probableCause

    def setProbableCause(self,value):
         self.probableCause = value   

    def getAlarmedObjectType(self):
        return self.probableCause

    def setAlarmedObjectType(self,value):
         self.probableCause = value   
   
    def getSpecificProblem(self):
        return self.specificProblem

    def setSpecificProblem(self,value):
         self.specificProblem = value 

    def getAlarmedObject(self):
        return self.alarmedObject

    def setalAlarmedObject(self,value):
         self.alarmedObject = value 

    def getSourceSystemId(self):
        return self.sourceSystemId

    def setSourceSystemId(self,value):
         self.sourceSystemId = value 

    def getAlarmDetails(self):
        return self.alarmDetails

    def setAlarmDetails(self,value):
         self.alarmDetails = value

    def getAlarmEscalation(self):
        return self.alarmEscalation

    def setAlarmEscalation(self,value):
         self.alarmEscalation = value

    def getAlarmRaisedTime(self):
        return self.alarmRaisedTime

    def setAlarmRaisedTime(self,value):
         self.alarmRaisedTime = value

    def getAlarmReportingTime(self):
        return self.alarmReportingTime

    def setAlarmReportingTime(self,value):
         self.alarmReportingTime = value

    def getAlarmClearedTime(self):
        return self.alarmClearedTime

    def setAlarmClearedTime(self,value):
         self.alarmClearedTime = value
    
    def getClearedTime(self):
        return self.clearedTime

    def setClearedTime(self,value):
         self.clearedTime = value

    def getAlarmChangedTime(self):
        return self.alarmChangedTime

    def setAlarmChangedTime(self,value):
         self.alarmChangedTime = value    
    
    def getAckSystemId(self):
        return self.ackSystemId

    def setAckSystemId(self,value):
         self.ackSystemId = value 

    def getAckUserId(self):
        return self.ackUserId

    def setAckUserId(self,value):
         self.ackUserId = value

    def getAckTime(self):
        return self.ackTime

    def setAckTime(self,value):
         self.ackTime = value

    def getAckState(self):
        return self.ackState

    def setAckState(self,value):
         self.ackState = value

    def getIsRoot(self):
        return self.isRoot

    def setIsRoot(self,value):
         self.isRoot = value

    def getParentAlarm(self):
        return self.parentAlarm

    def setParentAlarm(self,value):
         self.parentAlarm = value
    
    def getCorrelatedAlarm(self):
        return self.correlatedAlarm

    def setCorrelatedAlarm(self,value):
         self.correlatedAlarm = value
    
    def getComment(self):
        return self.comment

    def setComment(self,value):
         self.comment = value
