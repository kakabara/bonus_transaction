from pymodm import connection
from config import config

mongo_connect = connection.connect('mongodb://{user}:{password}@{host}:{port}/{db_name}'.format(**config['mongodb']))
