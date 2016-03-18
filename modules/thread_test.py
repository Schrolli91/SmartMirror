#-*- encoding: utf-8 -*-
"""
Simple Threading Modul Test
Autor: Bastian Schroll
"""

from tkinter import *
import logging
import time

from inc.modul import modul

class threadTest(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            print("Thread Test init")

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                print("Thread Test update")

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(1)
