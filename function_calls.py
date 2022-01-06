from pymongo import MongoClient

#client --> connecting to database
client = MongoClient("mongodb+srv://arkajit:arkajit@cluster0.dmii1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('Potato')
users_collection = db.users
listings_collection = db.listings
def login(email,password):
    user = users_collection.find_one({'email':email})
    if len(user)==0:
        return "no account associated with the given email"
    else:
        if password == user['password']:
            return "login"
        else:
            return "incorrect username or password"
print(login('arkajitdatta2010@gmail.com','12345678'))