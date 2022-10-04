import requests

url = "https://cdn-api.co-vin.in/api/v2/registration/certificate/public/download?beneficiary_reference_id=53391526641170"

payload={}
headers = {
  'Authorization': 'allow',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
