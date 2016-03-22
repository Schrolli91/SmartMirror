#-*- encoding: utf-8 -*-
"""
Wikipedia Search Modul
Autor: Bastian Schroll
"""

from tkinter import *
import logging

from inc.modul import modul

class wiki(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            print("Wiki init")
            

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                print("Wiki update")
                self.event.wait()

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(3)
