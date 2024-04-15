from app import app
from flask import jsonify, request, make_response
from utils.mogodbConnect import GetAndModifyMongoResults
from app import connection
import json
from bson import json_util
from flask.views import MethodView

from controllers.Accountview import AccountView

@app.route('/')
def index():
    return jsonify({"msg": "Hello World"})

    

app.add_url_rule('/accounts',view_func=AccountView.as_view('accounts_api'))