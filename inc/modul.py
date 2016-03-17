#-*- encoding: utf-8 -*-
"""

Autor: Bastian Schroll
"""
import logging
import threading
from inc.widget import widget



"""Container for the Modul"""
class modul(widget, threading.Thread):

    __modules = {} #all active modules

    def __init__(self, childName):
        widget.__init__(self, childName)
        threading.Thread.__init__(self)

        #Set Thread vars
        self.name = childName
        self.daemon = True

        self.__modules[self.name] = "?"

    def __del__(self):
        del self.__modules[self.name]

    def setStatus(self, name, status):
        """set the Status for an modul"""
        logging.debug("Status: %s %s", name, status)
        self.__modules[name] = status

    def getStatus(self, name):
        """get the Status for an modul"""
        return self.__modules[name]
