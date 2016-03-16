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
                logging.debug("update %s", __name__)

                ##############
                # code section

                print("Thread Test")
        
                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(1)

