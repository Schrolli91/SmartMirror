#-*- encoding: utf-8 -*-
"""
MirrorOS
simple OS for smart Mirrors

2016 by Bastian Schroll and Matthias Kittler
"""

from tkinter import *
import configparser
import logging

import threading
from modules.thread_test import threadTest

from inc.modul import modul

__version__ = "0.2-dev"
__buildDate___ = "none"

#configure the logger
logging.basicConfig(
    filename="log.txt",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(threadName)-18s %(module)-15s %(funcName)-12s [%(levelname)-8s] %(message)s",
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
        from modules.weather_json import jsonWeather
        from modules.log_view import viewer
        from modules.status import status
        from modules.news import news_focus
        from modules.welcome import welcome
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


        modules = []

        #modules.append(threadTest(root, config, 0,0))
        #modules.append(threadTest(root, config, 0,0))
        #modules.append(threadTest(root, config, 0,0))

        if config.getboolean("Modules","date"):
            modules.append(date(root, config, w-20, 60, "ne"))

        if config.getboolean("Modules","weather"):
            modules.append(jsonWeather(root,config,10,10,"nw"))

        if config.getboolean("Modules","clock"):
            modules.append(clock(root, config, w-10, 0, "ne"))

        if config.getboolean("Modules","log_view"):
            modules.append(viewer(root,config,10,h,"sw"))

        if config.getboolean("Modules","status"):
            modules.append(status(root,config,0,h/2,"w"))

        if config.getboolean("Modules","news"):
            modules.append(news_focus(root,config,w/2,h/2,"center"))

        if config.getboolean("Modules","welcome"):
            modules.append(welcome(root,config,w/2,150,"center"))

        for thr in modules:
            thr.daemon = True
            thr.start()


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
