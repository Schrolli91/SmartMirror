#-*- encoding: utf-8 -*-
"""
Thread Status Display for MirrorOS
Autor: Bastian Schroll
"""

import threading
import logging
import time

from inc.modul import modul

from tkinter import *

class status(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        threading.Thread.__init__(self)
        self.name = __name__
        self.daemon = True
        try:
            logging.debug("load %s", __name__)
            self.daemon = True

            #init self given args
            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

            self.active_threads = Label(self.window, fg=self.config.get("status","color"), font=self.config.get("status","font"), bg='black', justify="left")
            self.active_threads.place(x=self.xPos, y=self.yPos, anchor=self.anc)

        except:
            logging.exception("cannot load %s", __name__)


    def run(self):
        logging.debug("run %s", __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                self.thread_text = ""
                self.thread_text += "Threads running: " + str(threading.active_count()) + "\n"

                for t in threading.enumerate():
                	if t is "MainThread":
                		continue
                	self.thread_text += " - " + t.getName() + "\n"

                self.thread_text += "\n"
                for key, value in modul.getAllModules().items():
                    self.thread_text += "["+value+"] "+ key + "\n"

                self.active_threads.configure(text=self.thread_text)

            except:
                logging.exception("cannot read config file %s", __name__)
            finally:
                time.sleep(self.config.getfloat("status","update_interval"))
