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

from inc.modul import modul

class weather(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            self.addWidget("headline", Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","main_font"), bg='black'))
            self.addWidget("today_headline", Label(self.window, fg=self.config.get("weather","main_color"), font=self.config.get("weather","main_font"), bg='black'))
            self.addWidget("today_weather",  Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black', justify=LEFT))
            self.addWidget("today_icon", Label(self.window, bg="black"))
            self.addWidget("forecast_headline", Label(self.window, fg=self.config.get("weather","main_color"), font=self.config.get("weather","main_font"), bg='black'))
            self.addWidget("forecast_weather", Label(self.window, fg=self.config.get("weather","color"), font=self.config.get("weather","font"), bg='black', justify=LEFT))

            yStep = 22

            self.posWidget("headline", xPos, yPos, anc)
            self.posWidget("today_headline", xPos, yPos+yStep*1, anc)
            self.posWidget("today_weather", xPos, yPos+yStep*2, anc)
            self.posWidget("today_icon", xPos+160, yPos+25, anc)
            self.posWidget("forecast_headline", xPos, yPos+yStep*6, anc)
            self.posWidget("forecast_weather", xPos, yPos+yStep*7, anc)


            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):
            while 1: #infinite loop from thread - on exit, thread dies
                try:

                    ##############
                    # code section

                    self.weather_link = "http://api.openweathermap.org/data/2.5/weather?q="+ self.config.get("weather","city") +"&lang="+ self.config.get("weather","lang") +"&units=metric&appid="+ self.config.get("weather","api_key")
                    self.weather = self.fetch_json(self.weather_link)

                    self.forecast_link = "http://api.openweathermap.org/data/2.5/forecast/daily?q="+ self.config.get("weather","city") +"&lang="+ self.config.get("weather","lang") +"&units=metric&cnt=3&appid="+ self.config.get("weather","api_key")
                    self.forecast = self.fetch_json(self.forecast_link)

                    #############
                    #Weather today

                    if self.weather and self.forecast:
                        self.txtWidget("headline", "Wetterbericht für " + str(self.weather["name"]) +" ("+ str(self.weather["sys"]["country"]) +")")
                        self.txtWidget("today_headline", "Heutiges Wetter:")

                        self.txtWidget("today_weather",
                            str(self.weather["weather"][0]["description"]) +"\n"+
                            "Temperatur: "+ str(round(self.weather["main"]["temp"],1)) +" °C"+"\n"+
                            "Min: "+ str(round(self.forecast["list"][0]["temp"]["min"],1)) +" °C"+
                            "/ Max: "+ str(round(self.forecast["list"][0]["temp"]["max"],1)) +" °C"+"\n"+
                            "Luftfeuchte: "+ str(self.weather["main"]["humidity"]) +" %-rel."
                        )

                        self.icon = self.loadIcon(self.weather["weather"][0]["icon"])
                        self.getWidget("today_icon").configure(image=self.icon)

                    ##############
                    #Weather forecast

                    if self.forecast:
                        self.txtWidget("forecast_headline", "Vorhersage:")

                        self.txtWidget("forecast_weather",
                            "Morgen: "+ str(self.forecast["list"][1]["weather"][0]["description"]) +" ("+ str(round(self.forecast["list"][1]["temp"]["day"],1)) +"°C)\n"+
                            "Übermorgen: "+ str(self.forecast["list"][2]["weather"][0]["description"]) +" ("+ str(round(self.forecast["list"][2]["temp"]["day"],1)) +"°C)"
                            )



                    # code section
                    ##############

                except:
                    logging.exception("cannot update %s", __name__)
                finally:
                    self.wait(self.config.getfloat("weather","update_interval"))


    def fetch_json(self, link):
        try:
            logging.debug("fetch json from: %s", link)
            #get json weather data from today
            req = urllib.request.urlopen(link)
            encoding = req.headers.get_content_charset()
            logging.debug("fetching data is done")
            return json.loads(req.read().decode(encoding))

        except:
            logging.exception("cannot fetch data from web")
            return False


    def loadIcon(self, icon):
        try:
            logging.debug("load weather icon")
            #image loading
            return PhotoImage(file="modules/icons/"+ str(icon) +".gif")
        except:
            logging.exception("error while loading, set error.gif")
            return PhotoImage(file="modules/icons/error.gif")
