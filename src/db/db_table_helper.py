
from db.db_manager import DbManager

class DbTableHelper:
    
    def __init__(self,database, table, proxy_query=None):
        self.database = database
        self.table = table
        self.proxy_query = proxy_query

    def insert(self,data):
        row = DbManager.insert(self.database,self.table,data)
        return row

    def update(self,id, data):
        row = DbManager.update(self.database,self.table,id, data)
        return row

    def delete(self,id):
        row = DbManager.delete(self.database,self.table,id)
        return row
        
    def get_all(self,fields=None,offset=0,limit=200):
        rows = DbManager.get_all(self.database,self.table,fields=fields,offset=offset,limit=limit,proxy_query=self.proxy_query)
        return rows
    
    def get_by_id(self,id,fields=None):
        query = {"id" : id}
        row = DbManager.query(self.database,self.table,query,fields)
        return row
    
    def query(self,query,fields=None):
        row = DbManager.query(self.database,self.table,query,fields)
        return row
    
    def query_many(self,query,fields=None):
        row = DbManager.query_many(self.database,self.table,query,fields)
        return row