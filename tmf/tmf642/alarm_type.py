from enum import Enum

class AlarmType(Enum):
        unkownn = "unkownn"
        communicationsAlarm = "communicationsAlarm"
        processingErrorAlarm ="processingErrorAlarm"
        environmentalAlarm="environmentalAlarm"
        qualityOfServiceAlarm="qualityOfServiceAlarm"
        equipmentAlarm="equipmentAlarm"
        integrityViolation="integrityViolation"
        operationalViolation="operationalViolation"
        physicalViolation="physicalViolation"
        securityService="securityService"
        mechanismViolation="mechanismViolation"
        timeDomainViolation="timeDomainViolation"