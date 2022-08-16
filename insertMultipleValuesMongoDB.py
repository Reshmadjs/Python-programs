from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['firstDB']
collection=db['student']
# mylist=[
# { "_id":4,"name":"abc","Roll_no":8,"branch":"physics"},
# {"_id":5,"name":"pqr","Roll_no":9,"branch":"biology"},
# {"_id":6,"name":"xyz","Roll_no":10,"branch":"maths"},
# {"_id":7,"name":"mnc","Roll_no":11,"branch":"social science"}
# ]

# collection.insert_many(mylist)

mylist=[
 {"Manufacturer":"Honda", "Model":"City", "Color":"Black"},
  {"Manufacturer":"Tata", "Model":"Altroz", "Color":"Golden"},
  {"Manufacturer":"Honda", "Model":"Civic", "Color":"Red"},
  {"Manufacturer":"Hyundai", "Model":"i20", "Color":"white"},
  {"Manufacturer":"Maruti", "Model":"Swift", "Color":"Blue"}
]

collection.insert_many(mylist)