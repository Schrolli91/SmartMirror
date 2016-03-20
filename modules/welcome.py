#-*- encoding: utf-8 -*-
"""
welcome module for MirrorOS
Autor: Matthias Kittler, Bastian Schroll
"""

from tkinter import *
import time
import logging

from inc.modul import modul


class welcome(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            self.addWidget("welcome", Label(self.window, fg=self.config.get("welcome","color"), font=self.config.get("welcome","font"), bg='black'))
            self.posWidget("welcome", xPos, yPos, anc)

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):
        while 1:
            try:

                ##############
                # code section
                self.dayTime = time.strftime("%H:%M")

                #set default text
                self.welcome_text = self.config.get("welcome", "default")

                #check all entrys from config file
                for key, val in self.config.items("welcome"):
                    if "msg" in key:
                        msg = val.split(";")
                        if self.dayTime >= msg[0] and self.dayTime <= msg[1]:
                            self.welcome_text = msg[2]

                self.txtWidget("welcome", self.welcome_text)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(self.config.getfloat("clock","update_interval"))
