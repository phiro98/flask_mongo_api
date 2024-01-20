from flask import Flask
from os import environ
from flask_mongoengine import MongoEngine
from pymongo import MongoClient

app = Flask(__name__)
# MongoDB configuration with user credentials
mongodb_username = 'your_username'
mongodb_password = 'your_password'
mongodb_host = 'your_mongodb_host'  # Example: 'localhost' or 'mongodb.example.com'
mongodb_port = 'your_mongodb_port'  # Example: 27017
mongodb_database = 'your_database_name'
mongodb_uri = f'mongodb://{mongodb_username}:{mongodb_password}@{mongodb_host}:{mongodb_port}/{mongodb_database}'
app.config['SECRET_KEY']="ABC123"
db = MongoClient(mongodb_uri)


from flask1_mongo import routes
