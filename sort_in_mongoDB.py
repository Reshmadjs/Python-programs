from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['firstDB']
collection=db['student']
result=collection.find().sort("name",-1)
for i in result:
	print(i)