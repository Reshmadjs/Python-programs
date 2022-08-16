from pymongo import MongoClient
try:
	client=MongoClient('localhost',27017)
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")


db=client['secondDB']
collection=db['employee']

collection.update_many(
{"location":{"$regex":"^j"}},
{"$set":{"eid":4149}}

	)