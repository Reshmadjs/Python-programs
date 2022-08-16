from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['firstDB']
collection=db['student']


# performing queries to find Roll_no >9
query=collection.find({"Roll_no":{"$gte":9}})

# printing filtered data

for record in query:
	print(record)
print("*************************************")
cur=collection.find({"_id":{"$lte":3}})

for record in cur:
	print(record)