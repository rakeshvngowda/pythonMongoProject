from app import app
from flask import jsonify, request, make_response
from utils.mogodbConnect import GetAndModifyMongoResults
from app import connection
import json
from bson import json_util


@app.route('/')
def index():
    return jsonify({"msg": "Hello World"})


@app.route('/mongo')
def mongo():
    database = connection.database
    getResults = GetAndModifyMongoResults(database, 'accounts', {}, {"_id": 0})
    results = getResults.getResults()
    results = json.loads(json_util.dumps(results))
    return make_response(jsonify({"status":200, "results": results}), 200)
