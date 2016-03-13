#-*- encoding: utf-8 -*-
#########
#
# MirrorOS
# simple OS for smart Mirrors
#
# Version 0.1
# 2016 by Bastian Schroll and Matthias Kittler
#
############

from tkinter import *
import configparser
import logging


#configure the logger
logging.basicConfig(
    filename="log.txt",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(module)-15s %(funcName)-15s [%(levelname)-8s] %(message)s",
    datefmt = "%d.%m.%Y %H:%M:%S"
    )

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
        if config.getboolean("Modules","clock"):
            uhr = clock(root, config, w-10, 0, "ne") #build new clock

        if config.getboolean("Modules","date"):
            datum = date(root, config, w-20, 60, "ne") #build new date

        if config.getboolean("Modules","weather"):
            wetter_json = jsonweather(root,config,10,10,"nw") #build new weather
    except:
        logging.exception("cannot generate the modules")
        raise

    #photo = PhotoImage(file="png_icons/simple_weather_icon_12.png").subsample(5,5)
    #photo_label = Label(image=photo)
    #photo_label.place(x=500,y=50)
    #photo_label.image = photo

    root.mainloop()
except:
    logging.critical("MirrorOS ended by critical Error")
    print("MirrorOS ended by critical Error - see log.txt")
finally:
    logging.debug("clean up is done  - Quit()")
