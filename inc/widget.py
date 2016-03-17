#-*- encoding: utf-8 -*-
"""

Autor: Bastian Schroll
"""
import logging


"""Container for the Widgets"""
class widget():

    def __init__(self, childName):
        #Dict of all widgets
        self.__widgets = {}
        self.__childName = childName
        pass

    def __del__(self):
        del self.__widgets

    def addWidget(self, name, widget):
        """add a new widget with a name"""
        logging.debug("add new widget: %s %s", self.__childName, name)
        self.__widgets[name] = widget

    def delWidget(self, name):
        """delete the given widget"""
        self.hideWidget(name)
        logging.debug("delete widget: %s %s", self.__childName, name)
        del self.__widgets[name]

    def posWidget(self, name, xPos, yPos, anc):
        """set place for the given widget"""
        logging.debug("pos widget: %s %s", self.__childName, name)
        self.__widgets[name].place(x=xPos, y=yPos, anchor=anc)
        self.__widgets[name].pi = self.__widgets[name].place_info()

    def getWidget(self, name):
        """return the widget object"""
        return self.__widgets[name]

    def showWidget(self, name):
        """show the given widget"""
        logging.debug("show widget: %s %s", self.__childName, name)
        #show the widget at des saved palacement
        self.__widgets[name].place(self.__widgets[name].pi)

    def hideWidget(self, name):
        """hide the given widget"""
        logging.debug("hide widget: %s %s", self.__childName, name)
        #save the pace information in .pi
        self.__widgets[name].pi = self.__widgets[name].place_info()
        #forget the palacement -> hide
        self.__widgets[name].place_forget()
