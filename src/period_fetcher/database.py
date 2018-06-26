import os
from pymongo import MongoClient, errors
import report_topic

class Database:
    fetch_link = None
    data = None

    @classmethod
    def connect(cls, db_name):
        try:
            print("Connecting to database...")
            db = cls._connect(db_name)

            print("Connection successful")
            cls._create_collection(db)
            print("")

            return db

        except errors.ServerSelectionTimeoutError:
            print("Connection Timeout. Please Try again", 'red')
            exit(1)

    @classmethod
    def _connect(cls, db_name):
        cls._client = MongoClient()
        cls._client.server_info()

        db = cls._client[db_name]

        return db

    @classmethod
    def _create_collection(cls, db):
        cls.fetch_link = _Collection(db, 'fetch_link')
        cls.data = _Collection(db, 'data')
        if cls.fetch_link.count() == 0:
            cls._init_database(db)
    
    @classmethod
    def _init_database(cls, db):
        links = []
        for t in report_topic.report_link:
            for st in t['sub_topic']:
                st['main_topic'] = t['topic']
                links.append(st)

        db.fetch_link.insert_many(links)
            
        print("Database was initialized")

    @classmethod
    def disconnect(cls):
        if cls._client is not None:
            return cls._client.close()
        else:
            return None


class _Collection:
    def __init__(self, db, collection_name):
        self.collection = db[collection_name]

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def insert_many(self, data):
        return self.collection.insert_many(data)

    def find(self, find_params=None, return_field=None, limit=0):
        return self.collection.find(find_params, return_field).limit(limit)

    def find_one(self, find_params=None, return_field=None):
        return self.collection.find_one(find_params, return_field)

    def update_one(self, find_params, update):
        return self.collection.update_one(find_params, update)

    def count(self):
        return self.collection.count()

    def delete_one(self, find_params):
        return self.collection.delete_one(find_params)
    
    def save(self, update_obj):
        return self.collection.save(update_obj)

class _Queue(_Collection):
    def __init__(self, db, collection_name):
        super().__init__(db, collection_name)
