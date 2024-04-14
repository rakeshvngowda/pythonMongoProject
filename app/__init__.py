from flask import Flask
app = Flask(__name__)

from utils.mogodbConnect import MongoConnect

connection = MongoConnect('sample_analytics')
from app import routes

