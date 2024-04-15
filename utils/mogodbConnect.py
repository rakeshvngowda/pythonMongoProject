import pymongo
import json
import os
from bson import json_util
# from pymongo.errors import ConnectionError


class MongoConnect:
    def __init__(self, databaseName):
        try:
            self.databaseName = databaseName
            self.myclient = pymongo.MongoClient(os.getenv('MONGODB_URL'))
            self.database = self.myclient[databaseName]
            print('connected to database')
        except Exception as e:
            print(f"{e}")


class GetAndModifyMongoResults:
    def __init__(self, database, columnName):
        self.columnName = database[columnName]

    def getResults(self):
        results = list(self.columnName.find({}, {"_id": 0}).limit(5))
        return results
    
    def getSingleAccount(self,account_id):
        results = self.columnName.find_one({'account_id':account_id},{"_id":0})
        return results

    def insertresults(self, body):
        result = self.columnName.insert_one(body)
        return result

    def deleteResult(self, account_id):
        result = self.columnName.delete_one({'account_id': account_id})
        print(result)
        return
