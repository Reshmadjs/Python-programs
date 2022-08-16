# import json

# def write_json(new_data,filename='data.json'):
# 	with open(filename,'r+') as file:
# 		file_data=json.load(file)
# 		file_data["emp_details"].append(new_data)
# 		file.seek(0)
# 		json.dump(file_data,file,indent=4)
# 		print(file_data)	

# y = {"emp_name":"Nikhil",
#      "email": "nikhil@geeksforgeeks.org",
#      "job_profile": "Full Time"
#     }

# write_json(y)    




# importing the module
import json
 
# opening the JSON file
data = open('data.json',)
 
print("Datatype before deserialization : "
      + str(type(data)))
    
# deserializing the data
data = json.load(data)
 
print("Datatype after deserialization : "
      +str(type(data)))

