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

from inc.modul import modul

class news(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            self.addWidget("news", Label(self.window, fg=self.config.get("news","color"), font=self.config.get("news","font"), bg='black'))
            self.posWidget("news", xPos, yPos, anc)

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                self.newsText = self.fetch_data()
                self.txtWidget("news", self.newsText)

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                self.wait(self.config.getfloat("news","update_interval"))


    def fetch_data(self):
        try:
            logging.debug("load rss feed from web")
            tree = urllib.request.urlopen("http://rss.focus.de/fol/XML/rss_folnews_eilmeldungen.xml").read()

            tree = parseString(tree)

            title = tree.getElementsByTagName("title")

            self.__news_text = ""
            #start at 2 because the first two news are "FOCUS-Online-Eilmeldungen"
            for tit in range(2,self.config.getint("news","max_news")+2):
                self.__news_text += str(title[tit].firstChild.data) +"\n"

            return self.__news_text

        except:
            logging.exception("cannot load the rss feed from web")
