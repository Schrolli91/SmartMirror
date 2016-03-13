#-*- encoding: utf-8 -*-
"""
Calender module for MirrorOS
Autor: Matthias Kittler
"""

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from tkinter import *
import datetime
import logging

class calender
    def __init__(self, window, config, xPos, yPos, anc="n"):
        self.window = window
        self.config = config

        self.yStep = 22
        
        #label for the refresh info
        self.loading = Label(self.window, fg=self.config.get("calender","main_color"), font=self.config.get("calender","font"), bg='black')
        self.loading.place(x=xPos, y=yPos+10*self.yStep, anchor=anc)

        logging.debug("generated")
        self.update() #starts his own update routine

    def update(self):
        logging.debug("load new calender data")
        self.loading.configure(text="Aktualisiere Kalenderdaten ...")
        self.window.update() #redraw window
        self.fetch_data() #reload data from web
        self.loading.configure(text="")

        try:
            logging.debug("refresh the widgets")

            #refresh the widgets for todays birthdays
            

            #refresh the widgets for todays events
            

            #refresh the widgets for tomorrows birthdays
            

            #refresh the widgets for tomorrows events



        except:
            logging.exception("cannot refresh the data")

        self.window.after(self.config.getint("calender","update_interval"), self.update)








    def fetch_data(self):
        try:
            logging.debug("load todays entries")
            #get todays birthdays & events




            logging.debug("load tomorrows entires")
            #get tomorrows birthdays & events



        except:
            logging.exception("cannot fetch data from web")




        
