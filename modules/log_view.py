#-*- encoding: utf-8 -*-
"""
simple inMirror Logfile viewer for MirrorOS
Autor: Bastian Schroll
"""

import threading
import logging
import time

from tkinter import *

class viewer(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        threading.Thread.__init__(self)
        self.name = __name__
        self.daemon = True
        try:
            logging.debug("load " + __name__)
            self.daemon = True

            #init self given args
            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

            self.logfile = Label(self.window, fg=self.config.get("log_view","color"), font=self.config.get("log_view","font"), bg='black', justify="left")
            self.logfile.place(x=self.xPos, y=self.yPos, anchor=self.anc)

        except:
            logging.exception("cannot load " + __name__)


    def run(self):
        logging.debug("run " + __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                fileHandle = open ( 'log.txt',"r" )
                lineList = fileHandle.readlines()
                fileHandle.close()

                logfile_text = ""

                for line in range(10,0,-1):
                    logfile_text += str(len(lineList)-line) +"| "+ lineList[len(lineList)-line]

                self.logfile.configure(text=logfile_text)

            except:
                logging.exception("cannot read config file %s", __name__)
            finally:
                time.sleep(self.config.getfloat("log_view","update_interval"))
