from pymongo import MongoClient
import pymongo

class DbManager:

    @staticmethod
    def get_connection():
        connect_string = "mongodb://localhost:23017/"
        client = MongoClient(connect_string)
        return client
    
    @staticmethod
    def insert(database,table,data):
        data['_id'] = data['id']
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        collection.insert_one(data)
        client.close()
        return

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
    def get_by_id(database,table,id):
        client = DbManager.get_connection()
        db = client[database]
        collection = db[table]
        myquery = { "_id": id }
        data = collection.find_one(myquery)
        return data

    