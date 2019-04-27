import pymongo


MongoUri = "mongodb+srv://LeeCQ:1234@cluster0-l3jqa.azure.mongodb.net/Test?retryWrites=true"
client = pymongo.MongoClient(MongoUri)  # connect to Server.
db = client['Test']  # connect to db.
collection = db['book']  # open a collection.

collection.find()
collection.insert_one({'title': 'MongoDB', 'price': 99})  # add a data.

for b in collection.find():  # print some data from db.
    print(b)
