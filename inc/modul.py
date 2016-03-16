#-*- encoding: utf-8 -*-
"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""
import logging

class modul():
#"""Container for the Modules"""

    def __init__(self):
        #Dict of all widgets
        self.__widgets = {}
        pass

    def addWidget(self, name, widget):
        """add a new widget with a name"""
        logging.debug("add new widget: %s", name)
        self.__widgets[name] = widget

    def posWidget(self, name, xPos, yPos, anc):
        """set place for the given widget"""
        logging.debug("pos widget: %s", name)
        self.__widgets[name].place(x=xPos, y=yPos, anchor=anc)

    def getWidget(self, name):
        """return the widget object"""
        logging.debug("get widget: %s", name)
        return self.__widgets[name]

    def showWidget(self, name):
        """show the given widget"""
        logging.debug("show widget: %s", name)
        #show the widget at des saved palacement
        self.__widgets[name].place(self.__widgets[name].pi)

    def hideWidget(self, name):
        """hide the given widget"""
        logging.debug("hide widget: %s", name)
        #save the pace information in .pi
        self.__widgets[name].pi = self.__widgets[name].place_info()
        #forget the palacement -> hide
        self.__widgets[name].place_forget()
