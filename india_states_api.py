# Checking availability of corona vaccine using PIN

import requests

url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

payload={}
headers = {
  'accept': 'application/json',
  'Accept-Language': 'hi_IN'
}

response = requests.request("GET", url, headers=headers, data=payload)
raw_json=response.json()
# print(response.text)
print("-----------------------------------------------------------------------------------------------")
print("states")
for i in (raw_json['states']):
	print(i)


