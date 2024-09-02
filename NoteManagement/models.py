from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
database = client[Config.DATABASE]
notes = database['notes']
users = database['users']
