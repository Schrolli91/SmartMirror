#-*- encoding: utf-8 -*-
#########
#
# MirrorOS
# simple OS for smart Mirrors
#
# 2016 by Bastian Schroll and Matthias Kittler
#
############

from tkinter import *
import configparser
import logging

import threading
from modules.thread_test import threadTest

__version__ = "0.2-dev"
__buildDate___ = "none"

#configure the logger
logging.basicConfig(
    filename="log.txt",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(module)-15s %(funcName)-12s [%(levelname)-8s] %(message)s",
    datefmt = "%d.%m.%Y %H:%M:%S"
    )

logging.info("MirrorOS for Smart Mirrors")
logging.info("Version: " + __version__)
logging.info("Build Date: " + __buildDate___)

#Main program routine
try:
    #try to import modules
    try:
        logging.debug("import the modules")
        ##### Modules Import ######
        #
        from modules.clock import clock
        from modules.date import date
        from modules.weather_json import jsonweather
        from modules.log_view import viewer
        from modules.status import status
        #
        ##### Modules Import ######
    except:
        logging.exception("cannot import the modules")
        raise

    #try to read the config file
    try:
        logging.debug("read the config file")
        config = configparser.ConfigParser()
        config.read("config.ini")
    except:
        logging.exception("cannot read the config file")
        raise

    #try to generate tkinter window object
    try:
        logging.debug("generate the tkinter window")
        root = Tk()
        root.title("MirrorOS")

        w, h = root.winfo_screenwidth(), root.winfo_screenheight()#w and h for the display resolutions
        root.overrideredirect(1)#hide the window border
        root.geometry("%dx%d+0+0" % (w, h))#set the window size

        root.configure(background='black')#set background color
        root.bind("<Escape>", lambda e: e.widget.quit())#Escape Button to quit the window
    except:
        logging.exception("cannot generate the tkinter window")
        raise

    #show the MirrorOS Logo in the middle of the screen
    logo = Label(root, text="MirrorOS", fg="white", bg="black", font="Verdana 20 bold")
    logo.place(x=w, y=h, anchor=SE)

    #try to load the modules into tkinter window
    try:
        logging.debug("generate the modules")



        #for i in range(1,2):
        #    thread = threadTest(i)
        #    thread.start()


        if config.getboolean("Modules","date"):
            datum = date(root, config, w-20, 60, "ne") #build new date
            #datum.start()

        if config.getboolean("Modules","weather"):
            wetter_json = jsonweather(root,config,10,10,"nw") #build new weather

        if config.getboolean("Modules","clock"):
            uhr = clock(root, config, w-10, 0, "ne") #build new clock
            #uhr.start() #clock as thread

        if config.getboolean("Modules","log_view"):
            logfile_viewer = viewer(root,config,10,h,"sw")
            #logfile_viewer.start()

        if config.getboolean("Modules","log_view"):
            status_view = status(root,config,800,h,"sw")
            #status_view.start()

        uhr.start()
        datum.start()
        logfile_viewer.start()
        status_view.start()

    except:
        logging.exception("cannot generate the modules")
        raise

    logging.debug("tkinter mainloop started")
    root.mainloop()
except:
    logging.critical("MirrorOS ended by critical Error")
    print("MirrorOS ended by critical Error - see log.txt")
finally:
    logging.debug("clean up is done  - Quit()")
