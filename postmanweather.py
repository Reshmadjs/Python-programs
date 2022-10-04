import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=baramati&appid=4565e0b4f32851d1e692e5506ddd061d"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
