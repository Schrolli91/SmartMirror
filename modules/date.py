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
        self.window = window
        self.config = config

        self.date = Label(self.window, fg=self.config.get("date","color"), font=self.config.get("date","font"), bg='black')
        self.date.place(x=xPos, y=yPos, anchor=anc)

        logging.debug("generated")
        self.update() #starts his own update routine

    def update(self):
        logging.debug("update widget")
        self.date.configure(text=time.strftime(self.config.get("date","format")))
        self.date.after(self.config.getint("date","update_interval"), self.update)
