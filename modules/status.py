#-*- encoding: utf-8 -*-
"""
Thread Status Display for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import logging
import time

from inc.modul import modul

class status(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            self.addWidget("threads", Label(self.window, fg=self.config.get("status","color"), font=self.config.get("status","font"), bg='black', justify="left"))
            self.posWidget("threads", xPos, yPos, anc)

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                self.thread_text = "Activ Modules: "+ modul.cntAllModules() +"\n"

                for key, value in modul.getAllModules().items():
                    self.thread_text += "["+value[1]+"] "+ key + "\n"

                self.txtWidget("threads", self.thread_text)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                #here time.sleep() is used, to prevent for too many status update logs
                time.sleep(self.config.getfloat("status","update_interval"))
