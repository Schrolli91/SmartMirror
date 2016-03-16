#-*- encoding: utf-8 -*-
"""
Date module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging
import threading

class date(threading.Thread):
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


            self.date = Label(self.window, fg=self.config.get("date","color"), font=self.config.get("date","font"), bg='black')
            self.date.place(x=self.xPos, y=self.yPos, anchor=self.anc)

        except:
            logging.exception("cannot load %s", __name__)


    def run(self):
        logging.debug("run %s", __name__)
        while 1:
            try:
                logging.debug("update %s", __name__)

                date = time.strftime(self.config.get("date","format"))
                date = date.replace("Monday","Montag").replace("Tuesday","Dienstag").replace("Wednesday","Mittwoch")
                date = date.replace("Thursday","Donnerstag").replace("Friday","Freitag").replace("Saturday","Samstag").replace("Sunday","Sonntag")
                self.date.configure(text=date)

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("date","update_interval"))
