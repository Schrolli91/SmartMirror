#-*- encoding: utf-8 -*-
"""
welcome module for MirrorOS
Autor: Matthias Kittler
"""

from tkinter import *
import threading
import logging
import time

class welcome(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="n"):
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

            ##############
            # init section

            self.welcome  = Label(self.window, fg=self.config.get("welcome","color"), font=self.config.get("welcome","font"), bg='black')
            self.welcome.place(x=self.xPos, y=self.yPos, anchor=self.anc)

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def run(self):
        logging.debug("run %s", __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                logging.debug("update %s", __name__)

                ##############
                # code section
                self.dayTime = time.strftime
                print(self.dayTime)

                if self.dayTime >= 3*3600 and self.time <= 9*3600+29*60:
                    self.welcome_text = " Guten Morgen "
                elif self.dayTime >= 9*3600+30*60 and self.time <= 15*3600+59*60:
                    self.welcome_text = " Hallo "
                elif self.dayTime >= 16*3600 and self.time <= 2*3600+59*60:
                    self.welcome_text = " Guten Abend "
                else:
                    self.welcome1 = " Servus "
                self.welcome.configure(text=self.welcome_text)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("welcome","update_interval"))
