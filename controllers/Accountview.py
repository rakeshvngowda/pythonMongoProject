from flask import jsonify, request, make_response
from utils.mogodbConnect import GetAndModifyMongoResults
from app import connection
import json
from bson import json_util
from flask.views import MethodView


class AccountView(MethodView):
    def __init__(self):
        self.database = connection.database
        self.column = GetAndModifyMongoResults(self.database, 'accounts')

    def get(self):
        account_id = int(request.args.get('account_id'))
        if (account_id):
            results = self.column.getSingleAccount(account_id)
        else:
            results = self.column.getResults()
        results = json.loads(json_util.dumps(results))
        return make_response(jsonify({"status": 200, "results": results}), 200)

    def post(self):
        try:
            data = json.loads(request.data)
            insertData = GetAndModifyMongoResults(self.database, 'accounts')
            insertData.insertresults(data)
            return make_response(jsonify({"msg": "New record inserted Successfully"}), 201)
        except Exception as e:
            error = e.details.get('errmsg')
            return make_response(jsonify({"error": error}), 500)

    def put(self):
        return make_response(jsonify({"msg": "accounts creation put api"}), 201)

    def delete(self):
        account_id = int(request.args.get('account_id'))
        self.column.deleteResult(account_id)
        return make_response(jsonify({"msg": "accounts creation put api"}), 201)
