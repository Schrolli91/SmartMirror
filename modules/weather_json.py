#-*- encoding: utf-8 -*-
# Copyright by Kampis-Elektroecke
# Modified by Julian R.
# extended by Bastian Schroll & Matthias Kittler

from xml.dom.minidom import *
from tkinter import *
import urllib.request
import json


class jsonweather:
    def __init__(self, window, config, xPos, yPos, anc="n"):
        self.window = window
        self.config = config

        self.yStep = 22

        self.loading = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black')
        self.loading.place(x=xPos, y=yPos-30, anchor=anc)

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

        self.update()

    def update(self):
        self.loading.configure(text="Aktualisiere Wetterdaten ...")
        self.window.update() #redraw window
        self.fetch_data()
        self.loading.configure(text="")

        self.headline.configure(text="Wetterbericht für " + str(self.wetter["name"]) +" ("+ str(self.wetter["sys"]["country"]) +")")
        self.today.configure(text="Heutiges Wetter:")
        self.description.configure(text=self.wetter["weather"][0]["description"])
        self.temp.configure(text="Temperatur: "+ str(self.wetter["main"]["temp"]) +" °C")
        self.tempMinMax.configure(text="Min: "+ str(self.wetter["main"]["temp_min"]) +" °C Max: "+ str(self.wetter["main"]["temp_max"]) +" °C")
        self.pressure.configure(text="Luftdruck: "+ str(self.wetter["main"]["pressure"]) +" hPa")
        self.humidity.configure(text="Luftfeuchte: "+ str(self.wetter["main"]["humidity"]) +" %-rel.")


        self.window.after(self.config.get("weather","update_interval"), self.update)

    def fetch_data(self):

        req = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=rosstal&lang=de&units=metric&appid=f22b16242918f11f41f1f402fa612ffb')
        encoding = req.headers.get_content_charset()
        self.wetter = json.loads(req.read().decode(encoding))
