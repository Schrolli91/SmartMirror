#-*- encoding: utf-8 -*-
"""

Autor: Bastian Schroll
"""
import logging
import threading
from inc.widget import widget



"""Container for the Widgets"""
class modul(widget, threading.Thread):

    __modules = {}

    def __init__(self, childName):
        widget.__init__(self, childName)
        threading.Thread.__init__(self)
        self.name = childName
        self.daemon = True

        self.__modulStatus = {}
        self.__modules[childName] = "?"

    def setStatus(self, name, status):
        """set the Status for an modul"""
        logging.debug("Status: %s %s", name, status)
        self.__modules[name] = status

    def getStatus(self, name):
        """get the Status for an modul"""
        return self.__modules[name]

    def getModules(self):
        return self.__modules
