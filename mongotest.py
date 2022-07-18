import pymongo
client = pymongo.MongoClient("mongodb+srv://nikhilkp24:2408@nikhilkp2419.lrhpq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"nikhil",
    "email" : "nikhilns241@gamil.com",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)