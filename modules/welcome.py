#-*- encoding: utf-8 -*-
"""
welcome module for MirrorOS
Autor: Matthias Kittler
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

                if self.dayTime >= "03:00" and self.dayTime <= "09:29":
                    self.welcome_text = " Guten Morgen "
                elif self.dayTime >= "09:30" and self.dayTime <= "15:59":
                    self.welcome_text = " Hallo "
                elif self.dayTime >= "16:00" and self.dayTime >= "02:59":
                    self.welcome_text = " Guten Abend "
                else:
                    self.welcome_text = " Servus "

                self.txtWidget("welcome", self.welcome_text)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(self.config.getfloat("clock","update_interval"))
