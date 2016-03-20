#-*- encoding: utf-8 -*-
"""
Modul class for MirrorOS
Autor: Bastian Schroll
"""
import time
import logging
import threading
from inc.widget import widget


class modul(widget, threading.Thread):
    """Container for the Modul"""

    __modules = {} #all active modules
    __modulCtr = 0 #for uniqe modulname ID


    def __init__(self, childName):
        threading.Thread.__init__(self)
        #Set Thread vars
        self.name = str(self.__modulCtr) +"-"+ childName
        modul.__modulCtr += 1 #incr the modulCtr
        self.daemon = True

        widget.__init__(self, self.name)

        logging.debug("load new modul: %s", self.name)

        # 0 = module instance
        # 1 = status
        self.__modules[self.name] = [self, "?"]


    def run(self):
        """override the run method from the threading Module
        call the main, where must override in your own program
        when your main method ends, the module kill himself"""
        time.sleep(0.1) #wait a moment to start tkinter mainloop
        logging.debug("run %s", self.name)
        self.setStatus("R")
        self.main()
        #destruct the module instance
        logging.debug("kill modul: %s", self.name)
        del self.__modules[self.name]
        self.delAllWidgets() #run to kill all widgets

    def main(self):
        """For own code you must override with an cild method"""
        pass


    def wait(self, waitTime):
        """
        Wait for a given time - sets automaticly the status

        @param waitTime: time to wait in seconds
        """
        self.setStatus("S")
        time.sleep(float(waitTime))
        self.setStatus("R")

    def setStatus(self, status):
        """
        Set the Status of the Module

        @param status: staus as string
        """
        logging.debug("Status: %s [%s]", self.name, status)
        self.__modules[self.name][1] = status

    def getStatus(self):
        """Get the Status the Modul"""
        return self.__modules[self.name][1]

    #static method to return all modules and status
    def getAllModules():
        """Return the dict of all active modules with their status"""
        return modul.__modules

    #static method to return number of running modules
    def cntAllModules():
        """Return the number of all active modules"""
        return str(len(modul.__modules))
