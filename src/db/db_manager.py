from pymongo import MongoClient
import pymongo
import uuid
MAX_ROW_RETURN_COUNT=200
class DbManager:

    @staticmethod
    def get_unique_id():
        return str(uuid.uuid4())

    @staticmethod
    def get_connection():
        connect_string = "mongodb://localhost:23017/"
        client = MongoClient(connect_string)
        return client
    
    @staticmethod
    def insert(database,table,data):
        if "id" not in data:
            data['id'] = DbManager.get_unique_id()
        if data['id'] is None:
            data['id'] = DbManager.get_unique_id()
        data['_id'] = data['id']
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        collection.insert_one(data)
        client.close()
        row = DbManager.get_by_id(database,table,data['id'])
        return row

    @staticmethod
    def insert_many(database,table,list):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        collection.insert_many(list)
        client.close()
        return
    
    @staticmethod
    def update(database,table,id,data):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        myquery = { "_id": id }
        newvalues = { "$set": data }
        print(newvalues)
        collection.update_one(myquery, newvalues)
        return

    @staticmethod
    def delete_field(database,table,id,field_name):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        myquery = { "_id": id }
        data = {}
        data[field_name] = None
        delete_field = { "$unset": data }
        collection.update_one(myquery, delete_field)
        return
    @staticmethod
    def delete(database,table,id):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        myquery = { "_id": id }
        collection.delete_one(myquery)
        return

    @staticmethod
    def get_by_id(database,table,id):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        myquery = { "_id": id }
        data = collection.find_one(myquery)
        return data
    
    @staticmethod
    def get_all(database,table,fields=None,offset=0,limit=MAX_ROW_RETURN_COUNT,proxy_query=None):
        projection= None
        if fields is not None:
            projection = {}
            tokens = fields.split(",")
            for token in tokens:
                projection[token] = True
        if (offset is None):
            offset = 0
        if (limit is None):
            limit = MAX_ROW_RETURN_COUNT    
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        myquery = proxy_query
        rows = collection.find(myquery,projection=projection,skip=offset,limit=limit)
        data = []
        for row in rows:
          data.append(row)
        return data

    @staticmethod
    def query(database,table,query,fields=None):
        projection= None
        if fields is not None:
            projection = {}
            tokens = fields.split(",")
            for token in tokens:
                projection[token] = True
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        data = collection.find_one(query,projection=projection)
        return data
    @staticmethod
    def query_many(database,table,query,fields=None,offset=0,limit=MAX_ROW_RETURN_COUNT):
        projection= None
        if fields is not None:
            projection = {}
            tokens = fields.split(",")
            for token in tokens:
                projection[token] = True
        if (offset is None):
            offset = 0
        if (limit is None):
            limit = MAX_ROW_RETURN_COUNT   
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        data = collection.find(query,projection=projection,skip=offset,limit=limit)
        return data

    