from pymongo import MongoClient
try:
	client=MongoClient('localhost',27017)
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")


db=client['secondDB']
collection=db['employee']

records=[
{
	"name":"Mr.dilshad",
    "eid":30,
    "location":"bombay"
},

{
    "name":"Mr.jahagirdar",
    "eid":7,
    "location":"kashmir"
},
{
	
	"name":"Mr.shaikh",
    "eid":77,
    "location":"baramati"
}

]
collection.insert_many(records)
for record in collection.find():
	print(record)

query={"location":{"$regex":"^k"}}
d=collection.delete_many(query)
print(d.deleted_count,"documents deleted")

for i in collection.find():
	print(i)
