from flask import Flask
from os import environ
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
 

app = Flask(__name__)
# MongoDB configuration with user credentials
mongodb_username = environ.get('username')
mongodb_password = environ.get('password')
mongodb_host = 'your_mongodb_host'  # Example: 'localhost' or 'mongodb.example.com'
mongodb_port = 27017
mongodb_database = environ.get('db_name')
mongodb_uri = f'mongodb://{mongodb_username}:{mongodb_password}@{mongodb_host}:{mongodb_port}/{mongodb_database}'
app.config['SECRET_KEY']="ABC123"
db = MongoClient(mongodb_uri)


from flask1_mongo import routes
