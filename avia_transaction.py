from flask import Flask
from db_connection import mongo_connect


app = Flask(__name__)

from routes import *