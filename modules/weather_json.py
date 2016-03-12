#-*- encoding: utf-8 -*-
"""
Weather Modul for MirrorOS
based on the OpenWeatherMap API
fetch the weather data per json
and downloads the condition image
Autor: Bastian Schroll
"""

from xml.dom.minidom import *
from tkinter import *
import urllib.request
import json

#for the image download
from urllib.request import urlopen
import io
import base64


class jsonweather:
    def __init__(self, window, config, xPos, yPos, anc="n"):
        self.window = window
        self.config = config

        self.yStep = 22

        self.loading = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.loading.place(x=xPos, y=yPos+7*self.yStep, anchor=anc)

        self.headline = Label(self.window, fg=self.config.get("weather","main_color"), font=self.config.get("weather","main_font"), bg='black')
        self.headline.place(x=xPos, y=yPos, anchor=anc)
        self.today = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black')
        self.today.place(x=xPos, y=yPos+1*self.yStep, anchor=anc)

        self.description = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.description.place(x=xPos, y=yPos+2*self.yStep, anchor=anc)
        self.temp = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.temp.place(x=xPos, y=yPos+3*self.yStep, anchor=anc)
        self.tempMinMax = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.tempMinMax.place(x=xPos, y=yPos+4*self.yStep, anchor=anc)
        self.pressure = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.pressure.place(x=xPos, y=yPos+5*self.yStep, anchor=anc)
        self.humidity = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.humidity.place(x=xPos, y=yPos+6*self.yStep, anchor=anc)

        self.photo_label = Label(bg="black")
        self.photo_label.place(x=xPos+160,y=yPos+30)

        self.update()

    def update(self):
        self.loading.configure(text="Aktualisiere Wetterdaten ...")
        self.window.update() #redraw window
        self.fetch_data()
        self.loading.configure(text="")

        self.headline.configure(text="Wetterbericht für " + str(self.wetter["name"]) +" ("+ str(self.wetter["sys"]["country"]) +")")
        self.today.configure(text="Heutiges Wetter:")
        self.description.configure(text=self.wetter["weather"][0]["description"])
        self.temp.configure(text="Temperatur: "+ str(round(self.wetter["main"]["temp"],1)) +" °C")
        self.tempMinMax.configure(text="Min: "+ str(round(self.wetter["main"]["temp_min"],1)) +" °C / Max: "+ str(round(self.wetter["main"]["temp_max"],1)) +" °C")
        self.pressure.configure(text="Luftdruck: "+ str(round(self.wetter["main"]["pressure"])) +" hPa")
        self.humidity.configure(text="Luftfeuchte: "+ str(self.wetter["main"]["humidity"]) +" %-rel.")

        self.photo_label.configure(image=self.photo)
        self.photo_label.image = self.photo

        self.window.after(self.config.get("weather","update_interval"), self.update)

    def fetch_data(self):

        #get json weather data from today
        req = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ self.config.get("weather","city") +"&lang="+ self.config.get("weather","lang") +"&units=metric&appid="+ self.config.get("weather","api_key"))
        encoding = req.headers.get_content_charset()
        self.wetter = json.loads(req.read().decode(encoding))

        #image download
        image_url = "http://openweathermap.org/img/w/"+ str(self.wetter["weather"][0]["icon"]) +".png"
        image_byt = urlopen(image_url).read()
        image_b64 = base64.encodestring(image_byt)
        self.photo = PhotoImage(data=image_b64)
