#-*- encoding: utf-8 -*-
"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging

from inc.modul import modul


class clock(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            self.addWidget("clock", Label(window, fg=config.get("clock","color"), font=config.get("clock","font"), bg='black'))
            self.posWidget("clock", xPos, yPos, anc)

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):
        while 1:
            try:

                #self.getWidget("clock").configure(text=time.strftime(self.config.get("clock","format")))
                self.txtWidget("clock", time.strftime(self.config.get("clock","format")))

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(self.config.getfloat("clock","update_interval"))
