from pymongo import MongoClient
try:
	client=MongoClient('localhost',27017)
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")


db=client['secondDB']
collection=db['employee']
for i in collection.find().limit(2).skip(2):
	print(i)