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
        try:
            logging.debug("generate " + __name__)

            self.window = window
            self.config = config

            self.clock = Label(self.window, fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black')
            self.clock.place(x=xPos, y=yPos, anchor=anc)

            self.update() #starts his own update routine

        except:
            logging.exception("cannot generate " + __name__)


    def update(self):
        try:
            logging.debug("update " + __name__)

            self.clock.configure(text=time.strftime(self.config.get("clock","format")))
            self.clock.after(self.config.getint("clock","update_interval"), self.update)

        except:
            logging.exception("cannot update " + __name__)
