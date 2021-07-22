from enum import Enum

class AlarmPerceivedSeverity(Enum):
    critical = "critical"
    major = "major"
    minor = "minor"
    warning = "warning"
    indeterminate = "indeterminate"
    cleared = "cleared"
