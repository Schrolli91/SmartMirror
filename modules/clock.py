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


            self.addWidget("clock", Label(self.window, fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black'))
            self.posWidget("clock", xPos, yPos, anc)

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):
        logging.debug("run %s", __name__)


        #simple test for hide and show mechanism
        self.setStatus("R")
        self.getWidget("clock").configure(text=time.strftime(self.config.get("clock","format")))
        time.sleep(3)
        self.hideWidget("clock")
        time.sleep(3)
        self.posWidget("clock", 500,500,"n")
        self.showWidget("clock")
        time.sleep(3)
        self.delWidget("clock")
        self.setStatus("S")


        while 0:
            try:
                logging.debug("update %s", __name__)

                self.getWidget("clock").configure(text=time.strftime(self.config.get("clock","format")))

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("clock","update_interval"))
