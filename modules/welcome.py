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
            logging.debug("load " + __name__)

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
            logging.exception("cannot load " + __name__)


    def run(self):
        logging.debug("run " + __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                logging.debug("update " + __name__)

                ##############
                # code section
                self.time = time.strftime()
                self.welcome1
                if self.time >= 3*3600 and self.time <= 9*3600+29*60:
                    self.welcome1 = " Guten Morgen "
                elif self.time >= 9*3600+30*60 and self.time <= 15*3600+59*60:
                    self.welcome1 = " Hallo "
                elif self.time >= 16*3600 and self.time <= 2*3600+59*60:
                    self.welcome1 = " Guten Abend "
                else:
                    self.welcome1 = " Servus "
                self.welcome.configure(text=self.welcome1(self.config.get("welcome", "format")))
                
                # code section≈
                ##############

            except:
                logging.exception("cannot update " + __name__)
            finally:
                time.sleep(self.config.getfloat("welcome","update_intervall"))

