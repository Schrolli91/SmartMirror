#-*- encoding: utf-8 -*-
"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time
import logging
import threading

class clock(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
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

            self.clock = Label(self.window, fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black')
            self.clock.place(x=self.xPos, y=self.yPos, anchor=self.anc)

        except:
            logging.exception("cannot load " + __name__)


    def run(self):
        logging.debug("run " + __name__)
        while 1:
            try:
                logging.debug("update " + __name__)

                self.clock.configure(text=time.strftime(self.config.get("clock","format")))

            except:
                logging.exception("cannot update " + __name__)
            finally:
                time.sleep(self.config.getfloat("clock","update_interval"))
