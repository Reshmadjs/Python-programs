from pymongo import MongoClient
client=MongoClient('localhost',27017)
list_of_db = client.list_database_names()
 
if "firstDB" in list_of_db:
    print("Exists !!")
else:
    print("not exist")
