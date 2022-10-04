import requests

url = "localhost:8000/libraryapp/list/all"

payload={
  "username": "dilshad"
  "password": "mypassword"
}
headers = {
  'Cookie': 'csrftoken=XwBCu6lBO1DgaUPb2HraSRPyD7Qktisv101Fo4ZsGbrlBHCUPHMpSSRRNIhuB1Me'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
