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

#import the modules
from modules.clock import clock
from modules.date import date
from modules.weather import weather


#read the config file object
config = configparser.ConfigParser()
config.read("config.ini")

#generate the tkinter window object
root = Tk()
root.title("MirrorOS")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()#w and h for the display resolutions
root.overrideredirect(1)#hide the window border
root.geometry("%dx%d+0+0" % (w, h))#set the window size

root.configure(background='black')#set background color
root.bind("<Escape>", lambda e: e.widget.quit())#Escape Button to quit the window

#show the MirrorOS Logo in the middle of the screen
logo = Label(root, text="MirrorOS", fg="white", bg="black", font="Verdana 20 bold")
logo.place(x=w, y=h, anchor=SE)
footer = Label(root, text="quit with [ESC]", fg="gray", bg="black", font="Verdana 10 bold")
footer.place(x=w/2, y=h, anchor=S)


if config.getboolean("Modules","clock"):
    uhr = clock(root, config, w/2, 150) #build new clock

if config.getboolean("Modules","date"):
    datum = date(root, config, w/2, 210) #build new date

if config.getboolean("Modules","weather"):
    wetter = weather(root, config, w/10, 150) #build new date

root.mainloop()
