#-*- encoding: utf-8 -*-
"""
Date module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging

from inc.modul import modul

class date(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__)
        self.window = window
        self.config = config

        try:

            self.addWidget("date", Label(self.window, fg=self.config.get("date","color"), font=self.config.get("date","font"), bg='black'))
            self.posWidget("date", xPos, yPos, anc)

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
                self.txtWidget("date", date)

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(self.config.getfloat("date","update_interval"))
