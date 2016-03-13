#-*- encoding: utf-8 -*-
"""
Weather Modul for MirrorOS
based on the OpenWeatherMap API
fetch the weather data per json
and downloads the condition image
Autor: Bastian Schroll
"""

from tkinter import *
import logging

#for json download
import urllib.request
import json


class jsonweather:
    def __init__(self, window, config, xPos, yPos, anc="n"):
        self.window = window
        self.config = config

        self.yStep = 22

        #label for the refresh info
        self.loading = Label(self.window, fg=self.config.get("weather","main_color"), font=self.config.get("weather","font"), bg='black')
        self.loading.place(x=xPos, y=yPos+10*self.yStep, anchor=anc)

        #labels for todays weather
        self.headline = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black')
        self.headline.place(x=xPos, y=yPos, anchor=anc)

        self.main_today = Label(self.window, fg=self.config.get("weather","main_color"), font=self.config.get("weather","main_font"), bg='black')
        self.main_today.place(x=xPos, y=yPos+1*self.yStep, anchor=anc)
        self.weather_today = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black', justify=LEFT)
        self.weather_today.place(x=xPos, y=yPos+2*self.yStep, anchor=anc)

        self.icon_today = Label(self.window, bg="black")
        self.icon_today.place(x=xPos+160,y=yPos+25)

        #labels for the forecast
        self.main_forecast = Label(self.window, fg=self.config.get("weather","main_color"), font=self.config.get("weather","main_font"), bg='black')
        self.main_forecast.place(x=xPos, y=yPos+7*self.yStep, anchor=anc)
        self.weather_forecast = Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black', justify=LEFT)
        self.weather_forecast.place(x=xPos, y=yPos+8*self.yStep, anchor=anc)

        logging.debug("generated")
        self.update()

    def update(self):
        logging.debug("load new weather data")
        self.loading.configure(text="Aktualisiere Wetterdaten ...")
        self.window.update() #redraw window
        self.fetch_data() #reload data from web
        self.loading.configure(text="")

        try:
            logging.debug("refresh the widgets")
            #refresh the widgets for todays weather
            self.headline.configure(text="Wetterbericht für " + str(self.wetter["name"]) +" ("+ str(self.wetter["sys"]["country"]) +")")
            self.main_today.configure(text="Heutiges Wetter:")

            self.weather_today.configure(text=
                str(self.wetter["weather"][0]["description"]) +"\n"+
                "Temperatur: "+ str(round(self.wetter["main"]["temp"],1)) +" °C"+"\n"+
                "Min: "+ str(round(self.wetter["main"]["temp_min"],1)) +" °C / Max: "+ str(round(self.wetter["main"]["temp_max"],1)) +" °C"+"\n"+
                "Luftdruck: "+ str(round(self.wetter["main"]["pressure"])) +" hPa"+"\n"+
                "Luftfeuchte: "+ str(self.wetter["main"]["humidity"]) +" %-rel."
                )

            self.icon_today.configure(image=self.photo)
            self.icon_today.image = self.photo

            #refesh the widgets for weather forecast
            self.main_forecast.configure(text="Vorhersage:")

            self.weather_forecast.configure(text=
                "Morgen: "+ str(self.forecast["list"][0]["weather"][0]["description"]) +" ("+ str(round(self.forecast["list"][0]["temp"]["day"],1)) +"°C)\n"+
                "Übermorgen: "+ str(self.forecast["list"][1]["weather"][0]["description"]) +" ("+ str(round(self.forecast["list"][1]["temp"]["day"],1)) +"°C)"
                )
        except:
            logging.exception("cannot refresh the data")

        self.window.after(self.config.getint("weather","update_interval"), self.update)

    def fetch_data(self):
        try:
            logging.debug("load actual weather json for %s", self.config.get("weather","city"))
            #get json weather data from today
            req = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ self.config.get("weather","city") +"&lang="+ self.config.get("weather","lang") +"&units=metric&appid="+ self.config.get("weather","api_key"))
            encoding = req.headers.get_content_charset()
            self.wetter = json.loads(req.read().decode(encoding))

            logging.debug("load weather forecast json for %s", self.config.get("weather","city"))
            #get json weather forecast
            req = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?q="+ self.config.get("weather","city") +"&lang="+ self.config.get("weather","lang") +"&units=metric&cnt=2&appid="+ self.config.get("weather","api_key"))
            encoding = req.headers.get_content_charset()
            self.forecast = json.loads(req.read().decode(encoding))

            try:
                logging.debug("load weather icon")
                #image loading
                self.photo = PhotoImage(file="modules/icons/"+ str(self.wetter["weather"][0]["icon"]) +".gif")
            except:
                logging.exception("error while loading, set error.png")
                self.photo = PhotoImage(file="modules/icons/error.gif")

        except:
            logging.exception("cannot fetch data from web")
