from pymongo import MongoClient
import pymongo
import uuid

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
        collection.update_one(myquery, newvalues)
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
    def get_all(database,table):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        myquery = {}
        rows = collection.find(myquery)
        data = []
        for row in rows:
          data.append(row)
        return data

    @staticmethod
    def query(database,table,query):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        data = collection.find_one(query)
        return data
    @staticmethod
    def query_many(database,table,query):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        data = collection.find(query)
        return data

    