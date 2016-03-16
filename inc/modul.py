#-*- encoding: utf-8 -*-
"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""

class modul():
#"""Container for the Modules"""

    def __init__(self):
        self.__widgets = {}
        pass

    def addWidget(self, name, widget):
        """add a new widget with a name"""
        self.__widgets[name] = widget

    def posWidget(self, name, xPos, yPos, anc):
        """set place for the given widget"""
        self.__widgets[name].place(x=xPos, y=yPos, anchor=anc)

    def getWidget(self, name):
        """return the widget object"""
        return self.__widgets[name]


    def showWidget(self, name):
        """show the given widget"""
        #show the widget at des saved palacement
        self.__widgets[name].place(self.__widgets[name].pi)

    def hideWidget(self, name):
        """hide the given widget"""
        #save the pace information in .pi
        self.__widgets[name].pi = self.__widgets[name].place_info()
        #forget the palacement -> hide
        self.__widgets[name].place_forget()
