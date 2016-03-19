#-*- encoding: utf-8 -*-
"""
Weather Modul for MirrorOS
based on the OpenWeatherMap API
fetch the weather data per json
and show the condition image
Autor: Bastian Schroll
"""

from tkinter import *
import threading
import logging
import time

#for json download
import urllib.request
import json

class weather(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        threading.Thread.__init__(self)
        self.name = __name__
        self.daemon = True
        try:
            logging.debug("load %s", __name__)

            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

            ##############
            # init section

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

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def run(self):
        logging.debug("run %s", __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                logging.debug("update %s", __name__)

                ##############
                # code section

                self.loading.configure(text="Aktualisiere Wetterdaten ...")
                #self.window.update() #redraw window
                self.fetch_data() #reload data from web
                self.loading.configure(text="")

                logging.debug("refresh the widgets")
                #refresh the widgets for todays weather
                self.headline.configure(text="Wetterbericht für " + str(self.wetter["name"]) +" ("+ str(self.wetter["sys"]["country"]) +")")
                self.main_today.configure(text="Heutiges Wetter:")

                self.weather_today.configure(text=
                    str(self.wetter["weather"][0]["description"]) +"\n"+
                    "Temperatur: "+ str(round(self.wetter["main"]["temp"],1)) +" °C"+"\n"+
                    "Min: "+ str(round(self.forecast["list"][0]["temp"]["min"],1)) +" °C"+
                    "/ Max: "+ str(round(self.forecast["list"][0]["temp"]["max"],1)) +" °C"+"\n"+
                    "Luftdruck: "+ str(round(self.wetter["main"]["pressure"])) +" hPa"+"\n"+
                    "Luftfeuchte: "+ str(self.wetter["main"]["humidity"]) +" %-rel."
                    )

                #self.icon_today.configure(image=self.photo)
                #self.icon_today.image = self.photo

                #refesh the widgets for weather forecast
                self.main_forecast.configure(text="Vorhersage:")

                self.weather_forecast.configure(text=
                    "Morgen: "+ str(self.forecast["list"][1]["weather"][0]["description"]) +" ("+ str(round(self.forecast["list"][1]["temp"]["day"],1)) +"°C)\n"+
                    "Übermorgen: "+ str(self.forecast["list"][2]["weather"][0]["description"]) +" ("+ str(round(self.forecast["list"][2]["temp"]["day"],1)) +"°C)"
                    )

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("weather","update_interval"))


    def fetch_json(self, link):
        pass

    def fetch_data(self):
        try:
            logging.debug("load actual weather json for %s", self.config.get("weather","city"))
            #get json weather data from today
            req = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ self.config.get("weather","city") +"&lang="+ self.config.get("weather","lang") +"&units=metric&appid="+ self.config.get("weather","api_key"))
            encoding = req.headers.get_content_charset()
            self.wetter = json.loads(req.read().decode(encoding))

            logging.debug("load weather forecast json for %s", self.config.get("weather","city"))
            #get json weather forecast
            req = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?q="+ self.config.get("weather","city") +"&lang="+ self.config.get("weather","lang") +"&units=metric&cnt=3&appid="+ self.config.get("weather","api_key"))
            encoding = req.headers.get_content_charset()
            self.forecast = json.loads(req.read().decode(encoding))

            print(self.wetter)

            # try:
            #     logging.debug("load weather icon")
            #     #image loading
            #     self.photo = PhotoImage(file="modules/icons/"+ str(self.wetter["weather"][0]["icon"]) +".gif")
            # except:
            #     logging.exception("error while loading, set error.gif")
            #     self.photo = PhotoImage(file="modules/icons/error.gif")

        except:
            logging.exception("cannot fetch data from web")
