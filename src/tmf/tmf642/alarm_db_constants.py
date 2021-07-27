from enum import Enum

class AlarmDbConstants(Enum):
    DB_ALARM="DB_ALARM"
    TABLE_ALARM="alarm"
    TABLE_ACK_ALARM="ack_alarm"
    TABLE_UNACK_ALARM="unack_alarm"
    TABLE_CLEAR_ALARM="clear_alarm"
    TABLE_COMMENT_ALARM="comment_alarm"
    TABLE_GROUP_ALARM="group_alarm"
    TABLE_UNGROUP_ALARM="ungroup_alarm"
    TABLE_ALARM_EVENT="alarm_event"
    TABLE_ALARM_SUBSCRIPTION="alarm_event_subscription"
