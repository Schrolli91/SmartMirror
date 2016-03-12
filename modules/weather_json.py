#-*- encoding: utf-8 -*-
# Copyright by Kampis-Elektroecke
# Modified by Julian R.
# extended by Bastian Schroll & Matthias Kittler

from xml.dom.minidom import *
from tkinter import *
import urllib.request
import json


class jsonweather:
    def __init__(self):
        self.fetch_data()

    def fetch_data(self):

        req = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=rosstal&lang=de&units=metric&appid=f22b16242918f11f41f1f402fa612ffb')
        encoding = req.headers.get_content_charset()
        wetter = json.loads(req.read().decode(encoding))

        print(str(wetter["name"]) +" ("+ str(wetter["sys"]["country"]) +")")
        print("Sunrise:  "+ str(wetter["sys"]["sunrise"]) +" Uhr")
        print("Sunset:   "+ str(wetter["sys"]["sunset"]) +" Uhr")
        print(wetter["weather"][0]["description"])
        print("Temp:     "+ str(wetter["main"]["temp"]) +" °C")
        print("Temp Min: "+ str(wetter["main"]["temp_min"]) +" °C")
        print("Temp Max: "+ str(wetter["main"]["temp_max"]) +" °C")
        print("Druck   : "+ str(wetter["main"]["pressure"]) +" hPa")
        print("Feuchte : "+ str(wetter["main"]["humidity"]) +" % rel.")
        print("Temp Max: "+ str(wetter["main"]["temp_max"]) +" °C")


wetter = jsonweather()
#wetter.fetch_data()
