from pymongo import MongoClient
# make connection

client=MongoClient('localhost',27017)
db=client["firstDB"]

print("DB created")

collection=db["student"]

print("collection created")
record={
	
	"_id":1,
	"name":"dilshad",
	"roll_no":"1",
	"branch":"soft eng"
}

print("record inserition starting")
rec_insert=collection.insert_one(record)
print("record is inserted")