#-*- encoding: utf-8 -*-
"""

Autor: Bastian Schroll
"""
import time
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

        logging.debug("load new modul: %s", self.name)

        self.__modules[self.name] = "?"

    def run(self):
        """override the run method from the threading Module
        call the main, where must override in your own program
        when your main method ends, the module kill himself"""
        self.main()
        #destruct the module instance
        logging.debug("kill modul: %s", self.name)
        del self.__modules[self.name]
        self.delAllWidgets() #run to kill all widgets

    def main(self):
        """For own code you must override with an cild method"""
        pass


    def wait(self, waitTime):
        """Wait for a given time - sets automaticly the status"""
        self.setStatus("S")
        time.sleep(float(waitTime))
        self.setStatus("R")

    def setStatus(self, status):
        """Set the Status of the Module"""
        logging.debug("Status: %s [%s]", self.name, status)
        self.__modules[self.name] = status

    def getStatus(self):
        """Get the Status the Modul"""
        return self.__modules[self.name]

    #static method to return all modules and status
    def getAllModules():
        """Return the dict of all active modules with ther status"""
        return modul.__modules
