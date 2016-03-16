#-*- encoding: utf-8 -*-
"""
welcome module for MirrorOS
Autor: Matthias Kittler
"""

from datetime import datetime, time
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
                self.dayTime = time.strftime("%H:%M")
               

                if self.dayTime >= "03:00" and self.dayTime <= "09:29":
                    self.welcome_text = " Guten Morgen "
                elif self.dayTime >= "09:30" and self.dayTime <= "15:59":
                    self.welcome_text = " Hallo "
                elif self.dayTime >= "16:00" and self.dayTime <= "02:59":
                    self.welcome_text = " Guten Abend "
                else:
                    self.welcome_text = " Servus "

                self.welcome.configure(text=self.welcome_text)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("welcome","update_interval"))
