#-*- encoding: utf-8 -*-
"""
Date module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging

class date:
    def __init__(self, window, config, xPos, yPos, anc="n"):
        try:
            logging.debug("generate " + __name__)

            self.window = window
            self.config = config

            self.date = Label(self.window, fg=self.config.get("date","color"), font=self.config.get("date","font"), bg='black')
            self.date.place(x=xPos, y=yPos, anchor=anc)

            self.update() #starts his own update routine

        except:
            logging.exception("cannot generate " + __name__)


    def update(self):
        try:
            logging.debug("update " + __name__)

            date = time.strftime(self.config.get("date","format"))
            date = date.replace("Monday","Montag").replace("Tuesday","Dienstag").replace("Wednesday","Mittwoch")
            date = date.replace("Thursday","Donnerstag").replace("Friday","Freitag").replace("Saturday","Samstag").replace("Sunday","Sonntag")
            self.date.configure(text=date)
            self.date.after(self.config.getint("date","update_interval"), self.update)

        except:
            logging.exception("cannot update " + __name__)
