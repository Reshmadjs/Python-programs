from tkinter import *
from configparser import ConfigParser

from tkinter import messagebox        
# for showing popup messages

import requests

url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file='weather.key'
# in weather.key file weathervapi is stored

file_a=ConfigParser()
# ConfigParser is used to read api

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

def print_weather():
	city=search_city.get()
	weather=weather_find(city)
	if weather:
		location_entry['text']='{},{}'.format(weather[0],weather[1])
		temperature_entry['text']='{:.2f} C,{:.2f} F'.format(weather[2],weather[3])
		weather_entry['text']=weather[4]
	else:
		messagebox.showerror('Error','please enter valid city')	


def clear_text(self):
	self.entry.delete(0,'end')


root=Tk()
#made tkinter window here, then next give title to that window

root.title("Weather App")

root.config(background="black")
#for giving backgroundcolor

root.geometry("700x400")

search_city=StringVar()
#taken var search_city as string type and one text box as enter_city and in it, whatever we write is stored in search_city and font is given
enter_city=Entry(root,textvariable=search_city,fg="blue",font=("Arial",30,"bold"))

enter_city.pack()
# Tkinter literally packs all the widgets one after the other in a window.

search_button=Button(root,text='search',width=20,bg="red",fg="white",font=("Arial",25,"bold"),command=print_weather)
search_button.pack()
# for creating button 

clear_button=Button(root,text='clear',width=20,bg="red",fg="white",font=("Arial",25,"bold"),command=self.clear_text)
clear_button.pack()


location_entry=Label(root,text=" ",font=("Arial",35,"bold"),bg="lightblue")
location_entry.pack()

temperature_entry=Label(root,text=" ",font=("Arial",35,"bold"),bg="lightpink")
temperature_entry.pack()

weather_entry=Label(root,text=" ",font=("Arial",35,"bold"),bg="lightgreen")
weather_entry.pack()



root.mainloop()
# use to run our application. This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until you close the window where you called the method.


