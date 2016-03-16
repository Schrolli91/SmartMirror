#-*- encoding: utf-8 -*-
"""
Simple Threading Modul Test
Autor: Bastian Schroll
"""

from tkinter import *
import threading
import logging
import time

class threadTest(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
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

                print("Thread Test")

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(1)
