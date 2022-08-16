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
	"name":"Mr.Geek",
    "eid":24,
    "location":"delhi"
},

{
    "name":"Mr.Shaurya",
    "eid":14,
    "location":"delhi"
},
{
	
	"name":"Mr.Coder",
    "eid":14,
    "location":"gurugram"
}

]
collection.insert_many(records)
print("Before deletion data is:")
cursors=collection.find()
for j in cursors:
	print(cursors)
	

print("After deletion data is:")

cursor=collection.delete_one({"name":"Mr.Shaurya"})
for i in collection.find():
	print(i)
