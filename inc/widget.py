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
        pass

    def addWidget(self, name, widget):
        """add a new widget with a name"""
        logging.debug("add new widget: %s %s", name, self.__childName)
        self.__widgets[name] = widget

    def delWidget(self, name):
        """delete the given widget"""
        self.hideWidget(name)
        logging.debug("delete widget: %s", name)
        del self.__widgets[name]

    def posWidget(self, name, xPos, yPos, anc):
        """set place for the given widget"""
        logging.debug("pos widget: %s", name)
        self.__widgets[name].place(x=xPos, y=yPos, anchor=anc)

    def getWidget(self, name):
        """return the widget object"""
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
