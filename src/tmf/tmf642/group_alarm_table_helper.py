import sys, os.path

sys.path.append("./../../")
sys.path.append("./../")

from db.db_table_helper import DbTableHelper
from alarm_db_constants import AlarmDbConstants

class GroupAlarmTableHelper(DbTableHelper):
    def __init__(self):
        super(GroupAlarmTableHelper,self).__init__(AlarmDbConstants.DB_ALARM.value,AlarmDbConstants.TABLE_GROUP_ALARM.value)