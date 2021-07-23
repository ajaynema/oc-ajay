
import sys, os.path
sys.path.append("./..")

from db_manager import DbManager

if __name__ == '__main__':
     # data = {'id' : '1', 'name':'test-1'}
     # DbManager.insert("DB_ALARM","alarm",data)
      data = {'name':'test-2'}
      DbManager.update("DB_ALARM","alarm","1",data)
