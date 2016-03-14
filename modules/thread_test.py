import threading
import logging
import time

class threadTest(threading.Thread):
    def __init__(self, waitTime):
        threading.Thread.__init__(self)
        self.daemon = True
        self.waitTime = waitTime

    def run(self):
        for i in range(1,20):
            logging.debug("Name: %s - Counter: %d", self.name, i)
            time.sleep(self.waitTime /3)
