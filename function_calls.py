from pymongo import MongoClient

#client --> connecting to database
client = MongoClient("mongodb+srv://arkajit:arkajit@cluster0.dmii1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('Potato')
users_collection = db.users
listings_collection = db.listings

def login(email,password):
    #has to be completed
    