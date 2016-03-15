import threading
import logging
import time

class threadTest(threading.Thread):
    def __init__(self, waitTime):
        threading.Thread.__init__(self)
        self.daemon = True
        try:
            logging.debug("load " + __name__)

            self.daemon = True
            self.waitTime = waitTime

        except:
            logging.exception("cannot load " + __name__)


    def run(self):
        try:
            while 1:
                logging.debug("update %s", __name__)
                time.sleep(self.waitTime*2)

        except:
            logging.exception("cannot update %s", __name__)
