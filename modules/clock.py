#-*- encoding: utf-8 -*-
"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging
import threading

class clock(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="n"):
        threading.Thread.__init__(self)
        self.daemon = True
        try:
            logging.debug("generate " + __name__)

            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

        except:
            logging.exception("cannot generate " + __name__)

    def run(self):
        try:
            logging.debug("start thread " + self.name)
            self.clock = Label(self.window, fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black')
            self.clock.place(x=self.xPos, y=self.yPos, anchor=self.anc)

            self.update()
        except:
            logging.exception("cannot run " + __name__)


    def update(self):
        try:
            logging.debug("update " + __name__)

            self.clock.configure(text=time.strftime(self.config.get("clock","format")))

            self.t = threading.Timer(self.config.getint("clock","update_interval"),self.update)
            self.t.start()

        except:
            logging.exception("cannot update " + __name__)
