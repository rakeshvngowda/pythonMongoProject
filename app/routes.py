from app import app
from flask import jsonify, request, make_response
from utils.mogodbConnect import GetAndModifyMongoResults
from app import connection
import json
from bson import json_util
from flask.views import MethodView

@app.route('/')
def index():
    return jsonify({"msg": "Hello World"})

# @app.route('/accounts')
def mongo():
    database = connection.database
    getResults = GetAndModifyMongoResults(database, 'accounts', {}, {"_id": 0})
    results = getResults.getResults()
    results = json.loads(json_util.dumps(results))
    return make_response(jsonify({"status":200, "results": results}), 200)

class AccountView(MethodView):
    def __init__(self):
        self.database = connection.database
        
    def get(self):
        getResults = GetAndModifyMongoResults(self.database, 'accounts', {}, {"_id": 0})
        results = getResults.getResults()
        results = json.loads(json_util.dumps(results))
        return make_response(jsonify({"status":200, "results": results}), 200)
    
    def post(self):
        try:
            data = json.loads(request.data)
            insertData = GetAndModifyMongoResults(self.database,'accounts')
            insertData.insertresults(data)
            return make_response(jsonify({"msg":"New record inserted Successfully"}),201)
        except Exception as e:
            args = e.args()
            return make_response(jsonify({"Error":args}),500)


    def put(self):
        return make_response(jsonify({"msg":"accounts creation put api"}),201)
    

app.add_url_rule('/accounts',view_func=AccountView.as_view('accounts_api'))