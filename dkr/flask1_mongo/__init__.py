from flask import Flask
from os import environ
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://{}:{}@mongo-nodeport-svc:32000/{}'.format(environ.get('username'),environ.get('password'),environ.get('db_name'))
}
app.config['SECRET_KEY']="ABC123"
db = MongoEngine(app)

from flask1_mongo import routes
