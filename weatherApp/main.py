#key=c0f4bacd17b24aaca7d155455232906
#email:gabamo7559@eimatro.com

import requests
import json
import pyttsx3

speak=pyttsx3.init()

city=input("Enter the name of city :")

url=f"https://api.weatherapi.com/v1/current.json?key=c0f4bacd17b24aaca7d155455232906&q={city}"

result=requests.get(url)
# print(result.text)

wdic=json.loads(result.text)
x=wdic["current"]["condition"]["text"]
print("Condition:",x)
y=wdic["current"]["temp_c"]
print("Temperature in C:",y)

speak.say(f"The current temperature in {city} is {y} celcius")
speak.runAndWait()
