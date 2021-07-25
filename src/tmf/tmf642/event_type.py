from enum import Enum

class EventType(Enum):
    AlarmCreateEvent = "AlarmCreateEvent"
    AlarmAttributeValueChangeEvent="AlarmAttributeValueChangeEvent"
    AlarmStateChangeEvent="AlarmStateChangeEvent"
    AlarmDeleteEvent="AlarmDeleteEvent"

    AckAlarmsCreateEvent = "AckAlarmsCreateEvent"
    AckAlarmsStateChangeEvent = "AckAlarmsStateChangeEvent"
    
    UnAckAlarmsCreateEvent = "UnAckAlarmsCreateEvent"
    UnAckAlarmsStateChangeEvent = "UnAckAlarmsStateChangeEvent"

    ClearAlarmsCreateEvent = "ClearAlarmsCreateEvent"
    ClearAlarmsStateChangeEvent="ClearAlarmsStateChangeEvent"

    CommentAlarmsCreateEvent = "CommentAlarmsCreateEvent"
    CommentAlarmsStateChangeEvent = "CommentAlarmsCreateEvent"

    GroupAlarmsCreateEvent="GroupAlarmsCreateEvent"
    GroupAlarmsStateChangeEvent ="GroupAlarmsStateChangeEvent"

    UnGroupAlarmsCreateEvent = "UnGroupAlarmsCreateEvent"
    UnGroupAlarmsStateChangeEvent = "UnGroupAlarmsStateChangeEvent"
