#-*- encoding: utf-8 -*-
"""
simple inMirror Logfile viewer for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import logging

class viewer:
    def __init__(self, window, config, xPos, yPos, anc="n"):
        self.window = window
        self.config = config

        self.logfile = Label(self.window, fg=self.config.get("log_view","color"), font=self.config.get("log_view","font"), bg='black', justify="left")
        self.logfile.place(x=xPos, y=yPos, anchor=anc)

        logging.debug("generated")
        self.update() #starts his own update routine

    def update(self):
        try:
            fileHandle = open ( 'log.txt',"r" )
            lineList = fileHandle.readlines()
            fileHandle.close()

            logfile_text = ""

            for line in range(1,10):
                logfile_text += lineList[len(lineList)-line]

            self.logfile.configure(text=logfile_text)
            self.logfile.after(self.config.getint("log_view","update_interval"), self.update)
        except:
            logging.exception("cannot read logfile")
