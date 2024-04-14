import pymongo
import json
import os
from bson import json_util
# from pymongo.errors import ConnectionError
class MongoConnect:
    def __init__(self,databaseName):
        try:
            self.databaseName= databaseName
            self.myclient = pymongo.MongoClient(os.getenv('MONGODB_URL'))
            self.database = self.myclient[databaseName]
            print('connected to database')
        except Exception as e:
            print(f"{e}")

    def getResults(self,columnName,query={},values={},limit=5):
        column = self.database[columnName]
        results = list(column.find(query,values).limit(limit))

        return json.dumps(results,default=json_util.default)

class GetAndModifyMongoResults:
    def __init__(self,database,columnName,query={},fields={}):
        self.columnName = database[columnName]
        self.query = query
        self.fields = fields
    
    def getResults(self):
        results = list(self.columnName.find(self.query,self.fields).limit(5))
        return results