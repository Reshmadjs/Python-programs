from tkinter import *
from configparser import ConfigParser

from tkinter import messagebox        
# for showing popup messages

import requests

url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file='weather.key'
# in weather.key file weathervapi is stored

file_a=ConfigParser()
# ConfigParser is used to objectify file content

file_a.read(api_file)
api_key=file_a['api_key']['key']

#now here we extract only needed data from api
def weather_find(city):
	final=requests.get(url_api.format(city,api_key)) 
	if final:
		json_file=final.json()
		city=json_file["name"]
		country_name=json_file['sys']['country']
		k_temperature=json_file['main']['temp']
		c_temperature=k_temperature-273.15
		f_temperature=(k_temperature-273.15)*9/5+32
		weather_display=json_file['weather'][0]['main']
		result=(city,country_name,c_temperature,f_temperature,weather_display)
		return result
	else:
		return None

# def print_weather():
# 	city=search_city.get()
# 	weather=weather_find(city)
# 	if weather:
# 		location_entry['text']='{},{}'.format(weather[0],weather[1])
# 		temperature_entry['text']='{:.2f} C,{:.2f} F'.format(weather[2],weather[3])
# 		weather_entry['text']=weather[4]
# 	else:
# 		messagebox.showerror('Error','please enter valid city')	



city = input("enter city")
weather=weather_find(city)
print(weather)


