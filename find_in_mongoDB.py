from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['firstDB']
collection=db['student']
x=collection.find_one()
print(x)

print('******************************************************')
for x in collection.find({"name":"mnc"}):
	print(x)
