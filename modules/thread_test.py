import threading
import logging
import time

class threadTest(threading.Thread):
    def __init__(self, name, waitTime):
        threading.Thread.__init__(self)
        self.name = name
        self.waitTime = waitTime

    def run(self):
        for i in range(1,20):
            logging.debug("Name: %s - Counter: %d", self.name, i)
            time.sleep(self.waitTime /10)
