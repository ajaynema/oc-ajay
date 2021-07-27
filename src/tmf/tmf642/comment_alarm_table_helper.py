import sys, os.path

sys.path.append("./../../")
sys.path.append("./../")

from db.db_table_helper import DbTableHelper
from alarm_db_constants import AlarmDbConstants

class CommentAlarmTableHelper(DbTableHelper):
    def __init__(self):
        super(CommentAlarmTableHelper,self).__init__(AlarmDbConstants.DB_ALARM.value,AlarmDbConstants.TABLE_COMMENT_ALARM.value)