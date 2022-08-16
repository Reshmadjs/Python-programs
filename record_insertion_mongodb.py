from pymongo import MongoClient
client=MongoClient('localhost',27017)

db = client["firstDB"]
collection = db["student"]
records=[
	{

	"_id":2,
	"name":"reshma",
	"roll_no":"2",
	"branch":"SE"
	},
	{
    "_id":3,
	"name":"kajal",
	"roll_no":"3",
	"branch":"doctor"

	}
]

for record in records:
	print(record)
	collection.insert_one(record)
	print("record inserted")
	