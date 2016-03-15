#-*- encoding: utf-8 -*-
"""
Simple Threading Modul Test
Autor: Bastian Schroll
"""

import threading
import logging
import time

class threadTest(threading.Thread):
    def __init__(self, waitTime):
        threading.Thread.__init__(self)
        self.name = __name__
        self.daemon = True
        try:
            logging.debug("load " + __name__)
            self.daemon = True

            #init self given args
            self.waitTime = waitTime

        except:
            logging.exception("cannot load " + __name__)


    def run(self):
        logging.debug("run " + __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                logging.debug("update %s", __name__)
                time.sleep(self.waitTime*2)

            except:
                logging.exception("cannot update %s", __name__)
