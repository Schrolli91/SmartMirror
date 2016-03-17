#-*- encoding: utf-8 -*-
"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging
import threading

from inc.modul import modul


class clock(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container

        try:
            logging.debug("load %s", __name__)

            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

            self.addWidget("clock", Label(self.window, fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black'))
            self.posWidget("clock", self.xPos, self.yPos, self.anc)

        except:
            logging.exception("cannot load %s", __name__)


    def run(self):
        logging.debug("run %s", __name__)
        while 1:
            try:
                logging.debug("update %s", __name__)

                self.setStatus(__name__, "R")

                self.getWidget("clock").configure(text=time.strftime(self.config.get("clock","format")))

                #simple test for hide and show mechanism
                time.sleep(3)
                self.hideWidget("clock")
                time.sleep(3)
                self.posWidget("clock", 500,500,"n")
                self.showWidget("clock")
                time.sleep(3)
                self.delWidget("clock")

                self.setStatus(__name__, "S")

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("clock","update_interval"))
