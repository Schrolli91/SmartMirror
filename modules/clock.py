#-*- encoding: utf-8 -*-
"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging

class clock:
    def __init__(self, window, config, xPos, yPos, anc="n"):
        self.window = window
        self.config = config

        self.clock = Label(self.window, fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black')
        self.clock.place(x=xPos, y=yPos, anchor=anc)

        logging.debug("generated")
        self.update() #starts his own update routine

    def update(self):
        logging.debug("update widget")
        self.clock.configure(text=time.strftime(self.config.get("clock","format")))
        self.clock.after(self.config.getint("clock","update_interval"), self.update)
