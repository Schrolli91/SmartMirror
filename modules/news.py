#-*- encoding: utf-8 -*-
"""
Focus Eilmeldungen RSS News Feed Modul
Autor: Bastian Schroll
"""

from tkinter import *
import threading
import logging
import time

from xml.dom.minidom import *
import urllib.request

class news_focus(threading.Thread):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        threading.Thread.__init__(self)
        self.name = __name__
        self.daemon = True
        try:
            logging.debug("load %s", __name__)

            self.window = window
            self.config = config
            self.xPos = xPos
            self.yPos = yPos
            self.anc = anc

            ##############
            # init section

            self.news = Label(self.window, fg=self.config.get("news","color"), font=self.config.get("news","font"), bg='black')
            self.news.place(x=self.xPos, y=self.yPos, anchor=self.anc)

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def run(self):
        logging.debug("run %s", __name__)
        while 1: #infinite loop from thread - on exit, thread dies
            try:
                logging.debug("update %s", __name__)

                ##############
                # code section

                self.fetch_data()
                self.news.configure(text=self.news_text)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                time.sleep(self.config.getfloat("news","update_interval"))


    def fetch_data(self):
        try:
            logging.debug("load rss feed from web")
            tree = urllib.request.urlopen("http://rss.focus.de/fol/XML/rss_folnews_eilmeldungen.xml").read()

            tree = parseString(tree)

            title = tree.getElementsByTagName("title")

            self.news_text = ""
            #start at 2 because the first two news are "FOCUS-Online-Eilmeldungen"
            for tit in range(2,self.config.getint("news","max_news")+2):
                self.news_text += str(title[tit].firstChild.data) +"\n"

        except:
            logging.exception("cannot load the rss feed from web")
