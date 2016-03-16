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


class clock(threading.Thread, modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        threading.Thread.__init__(self)
        modul.__init__(self)
        self.name = __name__
        self.daemon = True
        try:
            logging.debug("load %s", __name__)

            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

            self.addWidget("clock", Label(self.window, text="test", fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black'))
            self.posWidget("clock", self.xPos, self.yPos, self.anc)

        except:
            logging.exception("cannot load %s", __name__)


    def run(self):
        logging.debug("run %s", __name__)
        while 1:
            try:
                logging.debug("update %s", __name__)

                self.getWidget("clock").configure(text=time.strftime(self.config.get("clock","format")))

                #simple test for hide and show mechanism
                time.sleep(3)
                self.hideWidget("clock")
                time.sleep(3)
                self.showWidget("clock")

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("clock","update_interval"))
