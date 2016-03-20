#-*- encoding: utf-8 -*-
"""
simple inMirror Logfile viewer for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import logging
import time

from inc.modul import modul

class viewer(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            self.addWidget("logfile", Label(self.window, fg=self.config.get("log_view","color"), font=self.config.get("log_view","font"), bg='black', justify="left"))
            self.posWidget("logfile", xPos, yPos, anc)

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                fileHandle = open ( 'log.txt',"r" )
                lineList = fileHandle.readlines()
                fileHandle.close()

                self.logfile_text = ""

                for line in range(self.config.getint("log_view", "max_lines"),0,-1):
                    self.logfile_text += str(len(lineList)-line).zfill(3) +"| "+ lineList[len(lineList)-line]

                self.txtWidget("logfile", self.logfile_text)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                #here time.sleep() is used, to prevent for too many status update logs
                time.sleep(self.config.getfloat("status","update_interval"))
