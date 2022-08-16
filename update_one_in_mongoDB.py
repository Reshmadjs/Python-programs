from pymongo import MongoClient
try:
	client=MongoClient('localhost',27017)
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")


db=client['secondDB']
collection=db['employee']
filter={"name":"Mr.Coder"}
newvalues={"$set":{"location":"goa"}}
collection.update_one(filter,newvalues)
for record in collection.find():
	print(record)