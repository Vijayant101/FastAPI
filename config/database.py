from pymongo import MongoClient, collection, database


client = MongoClient("mongodb+srv://user:Medika_123@test-db.krdwa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.todo_application #naming database as todo_application

collection_name = db['todos_app']

